class Car:

     def __init__(self,population_pm,attraction_pm,beauty_pm):
         self.population=population_pm
         self.attraction=attraction_pm
         self.beauty=beauty_pm
Japan=countri(population_pm="126500000",attraction_pm="вулкан Фудзияма.",beauty_pm=" страна с неповторимой культурой, одно из самых загадочных мест на земле. Отдых в Японии – это гора Фудзи и цветущая сакура, роботы XXI века и древние традиции, "
                                                                   "горнолыжные курорты с пушистым снегом и потрясающие пляжи. Около 80% территории страны – невысокие горы и плато, и только 10% –")
AQE=countri(population_pm="94410000",attraction_pm="Бурдж-Халифа",beauty_pm="")
total_sum=Japan.population_pm+AQE.population_pm
print(total_sum)