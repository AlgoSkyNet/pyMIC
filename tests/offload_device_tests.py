#!/usr/bin/python

# Copyright (c) 2014, Intel Corporation All rights reserved. 
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are 
# met: 
# 
# 1. Redistributions of source code must retain the above copyright 
# notice, this list of conditions and the following disclaimer. 
#
# 2. Redistributions in binary form must reproduce the above copyright 
# notice, this list of conditions and the following disclaimer in the 
# documentation and/or other materials provided with the distribution. 
#
# 3. Neither the name of the copyright holder nor the names of its 
# contributors may be used to endorse or promote products derived from 
# this software without specific prior written permission. 
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS 
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED 
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A 
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT 
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED 
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR 
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF 
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING 
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 

import unittest

import pyMIC as mic

device = mic.devices[0]        
device.load_library("libtests.so")

class OffloadDeviceTest(unittest.TestCase):
    """This class defines the test cases for the offload_device class."""
    
    def test_library_not_loaded(self):
        """Test if load_library throws an exception if a library cannot be loaded
           for any reason."""
        device = mic.devices[0]
        self.assertRaises(mic.OffloadException, device.load_library, "this_library_does_not_exist_anywhere")
        
    def test_invalid_kernel_name(self):
        """Test if invoke_kernel throws an exception if a kernel's name does
           not exist in any loaded library.
        """
        device = mic.devices[0]
        self.assertRaises(mic.OffloadException, device.invoke_kernel, "this_kernel_does_not_exist_anywhere")
    
    def test_invoke_empty_kernel(self):
        """Test if invoke_kernel does successfully invoke a kernel function
           with no arguments."""
        device = mic.devices[0]
        device.invoke_kernel("test_empty")
        