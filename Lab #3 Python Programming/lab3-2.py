def add_score(subject_score,student,subject, score):
  if subject_score.keys() :
    subject_score[student].update({subject:score})
  else : subject_score.update({student : {subject : score}})
  return subject_score 
def calc_average_score(subject_score):
  for key, value in subject_score.items():
    return {key : "{:.2f}".format(sum(value.values())/len(value.values()))}