record_collection = {
  2548: {
    'albumTitle': 'Slippery When Wet',
    'artist': 'Bon Jovi',
    'tracks': ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    'albumTitle': '1999',
    'artist': 'Prince',
    'tracks': ['1999', 'Little Red Corvette']
  },
  1245: {
    'artist': 'Robert Palmer',
    'tracks': []
  },
  5439: {
    'albumTitle': 'ABBA Gold'
  }
}

def update_records(record, id, property, value):
  if property  == "tracks"  and value != "" :
    try :
      if len(record[id][property]) >= 0 :
        record[id][property].append(value)
      else : record[id].update({property :[value]})
    except:
      record.update( {id : {property :[value]}})
  elif property  != ""  and value != "" :
      try : 
        record[id].update({property :value})
      except :record.update({id : {property :value}})
  elif  property  != ""  and value == "" :
      try :
        del record[id][property]  
      except :
        return record
  return record