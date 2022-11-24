#!/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         exportsetup.py
# Author:       Marcello Montaldo ( marcello.montaldo@gmail.com)
# Created:      2013/07/03
# Copyright:    Astra S.r.l.
# ------------------------------------------------------------------------------

import MySQLdb
import stormdb as adb
import Env

def Login(nomedb=None):
    if nomedb:
        Env.Azienda.DB.servername = 'localhost'
        Env.Azienda.DB.username   = 'x4user'
        Env.Azienda.DB.password   = 'x4user'
        Env.Azienda.DB._dbType    = 'mysql'
        conn = MySQLdb.connect(host=Env.Azienda.DB.servername,
                               user=Env.Azienda.DB.username,
                               passwd=Env.Azienda.DB.password,
                               db=nomedb,
                               use_unicode=True)
        conn.autocommit(True)
        Env.Azienda.DB.connection = conn
        db = adb.DB()
        db._dbCon = conn
        db.connected = True
        Env.Azienda.read_dati_azienda(db)
        retValue=True
    else:
        print 'Specificare nomedb'
        retValue=False
    return retValue

if Login('x4_impero'):
    dbAliquote = adb.DbTable('aliqiva', 'aliqiva', fields='id,codice,descriz')
    dbAliquote.SetDebug()
    dbAliquote.ClearOrders()
    dbAliquote.AddOrder('descriz', adb.ORDER_ASCENDING)
    dbAliquote.Retrieve()
    for r in dbAliquote:
        print r.id, r.codice, r.descriz