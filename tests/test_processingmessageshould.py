import json
import os
from http import HTTPStatus

from flask import request
import requests_mock

from src import main


def test_fail_when_method_is_not_supported(app):
  with app.test_request_context():
    result = main.fn_hook(request)
    assert result.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_fail_when_payload_is_missing(app):
    with app.test_request_context(path='/',
                                  method='POST',
                                  content_type='application/json'):
        result = main.fn_hook(request)
        assert result.status_code == HTTPStatus.BAD_REQUEST


def test_succeed(app):
  with app.test_request_context(path='/',
                                method='POST',
                                json={},
                                content_type='application/json'):
    result = main.fn_hook(request)
    assert result.status_code == HTTPStatus.OK
