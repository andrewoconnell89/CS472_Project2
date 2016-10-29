# Designed by Andy OConnell <aoconnel@bu.edu> <andrewoconnell89@gmail.com>

class CacheRow(object):
    """This contains the information in each row of cache."""
    def __init__(self, **kwargs):
        self.slot = 99
        self.valid = 0
        self.tag = 0
        self.data = [0]*16
        self.dirty = False

        #Fill in from kwargs
        if kwargs.get('slot') is not None:
            self.slot = kwargs.get('slot')
        if kwargs.get('valid') is not None:
            self.valid = kwargs.get('valid')
        if kwargs.get('tag') is not None:
            self.tag = kwargs.get('tag')
        if kwargs.get('dirty') is not None:
            self.dirty = kwargs.get('dirty')

    def __str__(self):
        result =   '{0:>6x}'+\
                    '{1:>6}'+\
                    '{2:>6x}'+\
                    '{3:>10x}'+\
                    '{4:>3x}'+\
                    '{5:>3x}'+\
                    '{6:>3x}'+\
                    '{7:>3x}'+\
                    '{8:>3x}'+\
                    '{9:>3x}'+\
                    '{10:>3x}'+\
                    '{11:>3x}'+\
                    '{12:>3x}'+\
                    '{13:>3x}'+\
                    '{14:>3x}'+\
                    '{15:>3x}'+\
                    '{16:>3x}'+\
                    '{17:>3x}'+\
                    '{18:>3x}'

        result = result.format( self.slot,
                                self.valid,
                                self.tag,
                                self.data[0],
                                self.data[1],
                                self.data[2],
                                self.data[3],
                                self.data[4],
                                self.data[5],
                                self.data[6],
                                self.data[7],
                                self.data[8],
                                self.data[9],
                                self.data[10],
                                self.data[11],
                                self.data[12],
                                self.data[13],
                                self.data[14],
                                self.data[15],)
        return result
