def playerHealth(health,name,level):
  healthMessage = name+" Lvl. "+str(level)+" ["

  for i in range(health):
    healthMessage+="-"
  for i in range((9 + level) - health):
    healthMessage+=" "

  healthMessage+="] " + str(health) + "/" + str(9+level)


  return healthMessage

def enemyHealthMessage(enemyName,enemyHealth,enemyFullHealth):
  healthMessage = enemyName + " ["

  for i in range(enemyHealth):
    healthMessage+="-"
  for i in range(enemyFullHealth - enemyHealth):
    healthMessage+=" "

  healthMessage+="] " + str(enemyHealth) + "/" + str(enemyFullHealth)


  return healthMessage
