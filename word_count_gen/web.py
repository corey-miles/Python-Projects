'''
    Class responsible for creating HTML file for
        word_count_gen.py.
'''

class MarkupParser():

    ##########
    ## INIT ##
    ##########

    '''
    @desc
        Initialization for MarkupParser.
    @param html
        String path to output html file.
    @param text
        String path to input txt file.
    @param words_dict
        Dictonary holding word counts.
    @param maximum
        Int current maximum count.
    @param minimum
        Int current minimum count.
    @param length
        Int number of terms to use in Tag Gen.
    '''
    def __init__(self, html, text, words_dict, maximum, minimum, length):
        self.html = html
        self.text = text
        self.words_dict = dict(words_dict)
        self.maximum = maximum
        self.minimum = minimum
        self.length = length

    ##############
    ## INSTANCE ##
    ##############

    '''
    @desc
        Util method for calculating the appropriate class-font size for a given count,
        assuming the current max and min of the data set.
    @param x
        Int number of occurances of a word.
    @return
        Int class-font size to use in HTML.
    '''
    def get_font_size(self, x):
        new_max = 11
        new_min = 48
        size = new_min
        if not self.maximum == self.minimum:
            size = (new_max - new_min)*(x - self.minimum)/(self.maximum - self.minimum) + new_min
        return int(size)

    '''
    @desc
        Creates insides of <head></head>
    @param sample
        File .html that is open.
    '''
    def create_head(self, sample):
        css = "http://web.cse.ohio-state.edu/software/2231/"
        css += "web-sw2/assignments/projects/tag-cloud-generator/data/tagcloud.css"
        sample.write("<title>Top " + str(self.length) + " words in " + self.text + "</title>\n")
        sample.write('<link href="' + css + '"\n')
        sample.write('rel="stylesheet" type="text/css">\n')

    '''
    @desc
        Creates insides of <body></body>
    @param sample
        File .html that is open.
    '''
    def create_body(self, sample):
        sample.write("<h2>Top " + str(self.length) + " words in " + self.text + "</h2>\n")
        sample.write("<hr>\n")
        sample.write('<div class="cdiv">\n')
        sample.write('<p class="cbox">\n')
        for key in self.words_dict:
            font = str(self.get_font_size(self.words_dict.get(key)))
            sample.write('<span style="cursor:default" class="f' + font + '" ')
            sample.write('title="count: ' + str(self.words_dict.get(key)) + '">' +key+ '</span>\n')
        sample.write("</p>\n")
        sample.write("</div>\n")

    '''
    @desc
        Creates .html file.
    '''
    def create_html(self):
        with open(self.html, 'w') as sample:
            sample.write("<head>\n")
            sample.write("<head>\n")
            self.create_head(sample)
            sample.write("</head>\n")
            sample.write("<body>\n")
            self.create_body(sample)
            sample.write("</body>\n")
            sample.write("</html>\n")
