# Copyright 2019, OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import time

try:
    time_ns = time.time_ns
# Python versions < 3.7
except AttributeError:

    def time_ns():
        return int(time.time() * 1e9)


def ns_to_iso_str(nanoseconds):
    """Get an ISO 8601 string from time_ns value."""
    ts = datetime.datetime.fromtimestamp(nanoseconds / 1e9)
    return ts.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
