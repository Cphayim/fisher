# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 15:25
"""
import json

from app import create_app

__author__ = 'Cphayim'

app = create_app()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], debug=app.config['DEBUG'])
