class Page:
    """
    A class with all the needed functions to prepare pages
    """

    def __init__(self, persons):
        self.base = persons

    @staticmethod
    def candidate(p):
        """
        Returns a string per each candidate, as this is used in all three pages
        :param p: person (a persons list entry as a dict)
        :return: a formatted string
        """
        return (f"Имя кандидата - {p.name}\n"
                f"{p.position}\n"
                f"{', '.join(p.skills)}\n")

    def home(self):
        s_list = []
        for p in self.base:
            s_list.append(Page.candidate(p))
        s = f"<pre>\n{'<br>'.join(s_list)}<br>\n</pre>\n"
        return s

    def candidates(self, num):
        s_list = []
        for p in self.base:
            if p.id == num:
                s_list.append(Page.candidate(p))
                s = f'<img src = "{p.picture}">\n\n<pre>\n{"<br>".join(s_list)}\n</pre>\n'
                return s
        return 'Candidate not found'

    def skills(self, skill):
        s_list = []
        for p in self.base:
            if skill.lower() in [skl.lower() for skl in p.skills]:
                s_list.append(Page.candidate(p))
        if s_list:
            return f"<pre>\n{'<br>'.join(s_list)}<br>\n</pre>\n"
        return f'No candidate found with skill: {skill}.'
