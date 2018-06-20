class Score(object):

    def getScore(self):
        return  self._score


    def setScore(self,value):
        if not isinstance(value,int):
            raise ValueError('value must be an integer!')

        if value<0 or value>100:
            raise ValueError('value must bettwen 0~100!')

        self._score=value



    # @property可以表示get

    @property
    def score(self):
         return self._score

    # set
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('value must be an integer!')

        if value < 0 or value > 100:
            raise ValueError('value must bettwen 0~100!')

        self._score = value



