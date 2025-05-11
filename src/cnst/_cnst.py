import json
import os

class Cnst():
  def __init__(self, pathname=None):
    if pathname is None:
      script_dir = os.path.dirname(os.path.realpath(__file__))
      pathname = os.path.join(script_dir, '_constants.json')
    with open(pathname, 'r') as fr:
      self.table = json.load(fr)

    self.table_names = [k for k in self.table if k!='shortcuts']
    self.all = {k:v[0] for t in self.table_names
        for k,v in self.table[t].items()}
    self.unit = {k:v[1] for t in self.table_names
        for k,v in self.table[t].items()}
    self.uncertainty = {k:v[2] for t in self.table_names
        for k,v in self.table[t].items()}
    self.reluncert = {k:u/v for (k,v),(k2,u) in
        zip(self.all.items(), self.uncertainty.items()) if k==k2 and v!=0}
    self.label = {k:f'{t} / {k}' for t in self.table_names
        for k,v in self.table[t].items()}

    for k,v in self.table['shortcuts'].items():
      try:
        entry = self.table[v[0]][v[1]]
        self.__dict__[k] = entry[0]
        self.all[k] = entry[0]
        self.unit[k] = entry[1]
        self.uncertainty[k] = entry[2]
        self.reluncert[k] = entry[2]/entry[0]
        self.label[k] = ' / '.join(v)
      except Exception as e:
        print(f'{k}: {v}', e)

    class _info():
      def __init__(self, cnst):
        self.cnst = cnst
      def __getitem__(self, key):
        d = {'value':self.cnst.all[key], 'label':self.cnst.label[key],
            'unit':self.cnst.unit[key],
            'uncertainty':self.cnst.uncertainty[key]}
        sc = [k for k,v in self.cnst.table['shortcuts'].items() if v[1] == key]
        if sc:
          d['shortcut'] = sc[0]
        return d
    self.info = _info(self)

  def __getitem__(self, key):
    return self.all[key]

  def search(self, s):
    keys = []
    if s in self.all:
      keys.append(s)
    keys.extend(sorted(
      [k for t in self.table_names for k,v in self.table[t].items()
      if (k not in keys) and (s.lower() in k.lower())],
      key=lambda k:(len(k), k)))
    return {k:self.info[k] for k in keys}

cnst = Cnst()

