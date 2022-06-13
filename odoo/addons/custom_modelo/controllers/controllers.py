# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class VisitController(http.Controller):

    @http.route('/app/tareas', auth='public', method=['GET'], csrf=False)
    def get_visits(self, **kw):
        try:
            visits = http.request.env['wb.todo'].sudo().search_read([], ['name','status','description'])
            res = json.dumps(visits, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    # Template echo en react.js
    @http.route('/app/pruebas', auth='public',website=True)
    def pruebas(self, **kw):
        return  http.request.render('custom_modelo.report_visit_pruebas',{})
