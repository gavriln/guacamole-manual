# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# Project, version, and author information
#

project = u'Apache Guacamole'
version = u'1.3.0'

copyright = u'2021, The Apache Software Foundation'
author = u'The Apache Software Foundation'

#
# Global options
#

extensions = [
    'myst_parser',
    'sphinx.ext.ifconfig',
    'sphinx.ext.extlinks'
]

# Allow shorthand notation for JIRA issue links
extlinks = {
    'jira': ( 'https://issues.apache.org/jira/browse/%s', '')
}

# Do not highlight source unless a Pygments lexer name is explicitly provided
highlight_language = 'none'

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "replacements",
    "smartquotes",
    "substitution"
]

myst_substitutions = {
    "version" : version
}

#
# HTML output options
#

html_theme = 'sphinx_rtd_theme'
html_title = u'Apache Guacamole Manual v%s' % version

