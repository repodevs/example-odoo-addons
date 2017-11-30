# -*- coding: utf-8 -*-
# © 2017 - TODAY Edi Santoso <repodevs@gmail.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

import json
from odoo import http
from odoo.http import request, Response
from odoo.exceptions import AccessDenied
from datetime import datetime, timedelta


def _helper(self, data):
	raise NotImplementedError()


class ApiTraining(http.Controller):
	"""API Training"""

	def _validate_key(self, data):
		""" Validate Api Key
		"""
		key = data.get('api_key', False)
		if key:
			user = request.env['res.users'].sudo().search([('api_key', '=', key)])
			if not user:
				Response.status = '400'
				raise AccessDenied()
				# return self._resp({"status": "error", "message": "wrong `api_key`"}, status=400)
			return user
		return False

	def _resp(self, data=None, status=200):
		"""
		Custom Response for inherit status code
		"""
		Response.status = str(status)
		return data


	@http.route('/api/training/create', type="json", auth="public",
				methods=['POST'], csrf=False)
	def api_training_create(self, **kwargs):
		"""
		Create Training from API

		@params	- name: name
				- description: description

		@returns json
		"""
		user = self._validate_key(request.jsonrequest)
		res = self._save_training(request.jsonrequest, user)
		return res


	@http.route('/api/training/update', type="json", auth="public",
				methods=['PUT'], csrf=False)
	def api_training_update(self, **kwargs):
		"""
		Update data from API

		@params	- id: id
				- name:	name
				- description: description

		@returns json
		"""
		user = self._validate_key(request.jsonrequest)
		res = self._update_training(request.jsonrequest, user)
		return res


	@http.route('/api/training/delete', type="json", auth="public",
				methods=['DELETE'], csrf=False)
	def api_training_delete(self, **kwargs):
		"""
		Delete data from API

		@params	- id:	id data

		@returns json
		"""
		user = self._validate_key(request.jsonrequest)
		res = self._delete_training(request.jsonrequest, user)
		return res


	def _save_training(self, data, user):
		""" Hook Save Training 
		"""
		trnObj = request.env['training.training']
		name = data.get('name', False)
		if not name:
			# send 400 status_code and error message
			# Response.status = '400'
			# return {"status": "error", "message": "`name` must filled"}
			return self._resp({"status": "error", "message": "`name` must filled"}, status=400)
		description = data.get('description', False)
		vals = {
			'name': name,
			'description': description,
		}
		training = trnObj.create(vals)
		if training:
			return self._resp({"status": "success", "data": {"training_id": training.id}}, status=200)

		return self._resp({"status": "error", "message": "unknown error"}, status=400)


	def _update_training(self, data, user):
		""" Hook Update Training
		"""
		vals = {}
		trnObj = request.env['training.training']
		training_id = data.get('id', False)
		name = data.get('name', False)
		description = data.get('description', False)
		if not training_id:
			return self._resp({"status": "error", "message": "`id` training not provided"}, status=400)
		if name:
			vals['name'] = name
		if description:
			vals['description'] = description

		check_id = trnObj.search_count([('id', '=', int(training_id))])
		if check_id == 0:
			return self._resp({"status": "error", "message": "error `id` not exists"}, status=400)

		update = trnObj.browse(int(training_id)).write(vals)
		if update:
			return self._resp({"status": "success", "data": vals}, status=200)

		return self._resp({"status": "error", "message": "unknown error"}, status=400)


	def _delete_training(self, data, user):
		""" Hook Delete Training
		"""
		trnObj = request.env['training.training']
		training_id = data.get('id', False)
		if not training_id:
			return self._resp({"status": "error", "message": "`id` not provided"}, status=400)

		check_id = trnObj.search_count([('id', '=', int(training_id))])
		if check_id == 0:
			return self._resp({"status": "error", "message": "`id` not exists"}, status=400)

		delete = trnObj.browse(int(training_id)).unlink()
		if delete:
			return self._resp({"status": "success", "message": "data `{}` successfully deleted".format(int(training_id))})

		return self._resp({"status": "error", "message": "unknown error"}, status=400)

