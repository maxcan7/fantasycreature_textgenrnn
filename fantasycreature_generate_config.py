#!/usr/bin/env py
import fantasycreature_pretrain_config as ptcfg

configpath = ptcfg.pretrain_cfg['mainpath'] + 'config/'
modelname = ptcfg.pretrain_cfg['modelname']

gen_cfg = {'weights': configpath + modelname + '_weights.hdf5', 'vocab': configpath + modelname + '_vocab.json', 'config': configpath + modelname + '_config.json', 'modelname': modelname}