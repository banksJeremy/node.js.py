#!/usr/bin/env python2.6
# standard
import threading
import sys
import os
import os.path
import subprocess
import shutil
# dependencies 
import nodeenv
# local
from _server import Server

class Node(object):
    node_version = "0.4.8"
    npm_version = "1.0.11"
    
    def __init__(self, dependencies=None, node_version=None, path_prefix=None,
                 npm_version=None, daemon=True):
        if node_version:
            self.node_version = str(node_version)
        
        if npm_version:
            self.npm_version = str(npm_version)
        
        self.dependencies = dependencies or []
        
        self.path = os.path.join(path_prefix or ".nodeenv",
                                 self.node_version, self.npm_version)
        
        self.daemon = daemon
        
        self._initialize_nodeenv()
        self._spawn_server_thread()
        self._spawn_node_process()
    
    def _initialize_nodeenv(self):
        class nodeenv_options(object):
            node = self.node_version
            npm = self.npm_version
            jobs = 2
            without_ssl = False
            without_npm = False
            no_npm_clean = False
            debug = False
            quiet = False
            verbose = False
            profile = False
            verbose = False
            prompt = None
            requirements = None
        
        if not os.path.exists(os.path.join(self.path, "_ready")):
            if os.path.exists(self.path):
                # remove previous failed initialization
                shutil.rmtree(self.path)
            
            nodeenv.create_environment(self.path, nodeenv_options)
            open(os.path.join(self.path, "_ready"), "w").close()
        
        activate_path = os.path.join(self.path, "bin", "activate")
        for package in self.dependencies:
            nodeenv.callit(cmd=['. '+ activate_path + 
                                " && " + "npm install " + package +
                                " && " + "npm activate " + package],
                           in_shell=True)
    
    def _spawn_server_thread(self):
        self.server = Server()
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.daemon = self.daemon
        self.thread.start()
    
    def _spawn_node_process(self):
        self.process = None
        
    