
# Copyright 2017 Intel Corporation
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
# -----------------------------------------------------------------------------

import dredd_hooks as hooks


@hooks.before("/api/proposals/{id} > PATCH > 200 > application/json")
def skip_proposal_update(txn):
    txn['skip'] = True


@hooks.before("/api/roles/{id} > PATCH > 200 > application/json")
def skip_roles_update(txn):
    txn['skip'] = True


@hooks.before("/api/roles/{id}/admins > DELETE > 200 > application/json")
def skip_del_role_admin(txn):
    txn['skip'] = True


@hooks.before("/api/roles/{id}/members > DELETE > 200 > application/json")
def skip_del_role_member(txn):
    txn['skip'] = True


@hooks.before("/api/roles/{id}/owners > DELETE > 200 > application/json")
def skip_del_role_owners(txn):
    txn['skip'] = True


@hooks.before("/api/roles/{id}/tasks > DELETE > 200 > application/json")
def skip_del_role_tasks(txn):
    txn['skip'] = True


@hooks.before("/api/tasks/{id} > PATCH > 200 > application/json")
def skip_task_update(txn):
    txn['skip'] = True


@hooks.before("/api/tasks/{id}/admins > DELETE > 200 > application/json")
def skip_del_task_admin(txn):
    txn['skip'] = True


@hooks.before("/api/tasks/{id}/owners > DELETE > 200 > application/json")
def skip_del_task_owners(txn):
    txn['skip'] = True