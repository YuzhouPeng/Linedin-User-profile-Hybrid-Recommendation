import remove_non_alphapet,re
class LinkedInData(object):

    def __init__(self, id, name, connections, title, org_summary, org_detail, duration, location, description,
                 past_job_title1, past_job_org_summary1, past_job_org_detail1, past_job_duration1, past_job_location1,
                 past_job_description1,
                 past_job_title2, past_job_org_summary2, past_job_org_detail2, past_job_duration2, past_job_location2,
                 past_job_description2,
                 past_job_title3, past_job_org_summary3, past_job_org_detail3, past_job_duration3, past_job_location3,
                 past_job_description3,
                 past_job_title4, past_job_org_summary4, past_job_org_detail4, past_job_duration4, past_job_location4,
                 past_job_description4,
                 past_job_title5, past_job_org_summary5, past_job_org_detail5, past_job_duration5, past_job_location5,
                 past_job_description5,
                 past_job_title6, past_job_org_summary6, past_job_org_detail6, past_job_duration6, past_job_location6,
                 past_job_description6,
                 highestLevel_universityName, highestLevel_degree, highestLevel_major,
                 highestLevel_endDate, highestLevel_detail,
                 otherLevel_universityName1, otherLevel_degree1, otherLevel_major1, otherLevel_endDate1,
                 otherLevel_detail1,
                 otherLevel_universityName2, otherLevel_degree2, otherLevel_major2, otherLevel_endDate2,
                 otherLevel_detail2,
                 otherLevel_universityName3, otherLevel_degree3, otherLevel_major3, otherLevel_endDate3,
                 otherLevel_detail3,
                 skills, languages):
        self.id = id
        self.name = name
        self.connections = connections
        self.title = title
        self.org_summary = org_summary
        self.org_detail = org_detail
        self.duration = duration
        self.location = location
        self.description = description
        self.past_job_title1, self.past_job_org_summary1, self.past_job_org_detail1, \
        self.past_job_duration1, self.past_job_location1, \
        self.past_job_description1 = past_job_title1, past_job_org_summary1 \
            , past_job_org_detail1, past_job_duration1, past_job_location1, past_job_description1
        self.past_job_title2, self.past_job_org_summary2, self.past_job_org_detail2, \
        self.past_job_duration2, self.past_job_location2, \
        self.past_job_description2 = past_job_title2, past_job_org_summary2 \
            , past_job_org_detail2, past_job_duration2, past_job_location2, past_job_description2
        self.past_job_title3, self.past_job_org_summary3, self.past_job_org_detail3, \
        self.past_job_duration3, self.past_job_location3, \
        self.past_job_description3 = past_job_title3, past_job_org_summary3 \
            , past_job_org_detail3, past_job_duration3, past_job_location3, past_job_description3
        self.past_job_title4, self.past_job_org_summary4, self.past_job_org_detail4, \
        self.past_job_duration4, self.past_job_location4, \
        self.past_job_description4 = past_job_title4, past_job_org_summary4 \
            , past_job_org_detail4, past_job_duration4, past_job_location4, past_job_description4
        self.past_job_title5, self.past_job_org_summary5, self.past_job_org_detail5, \
        self.past_job_duration5, self.past_job_location5, \
        self.past_job_description5 = past_job_title5, past_job_org_summary5 \
            , past_job_org_detail5, past_job_duration5, past_job_location5, past_job_description5
        self.past_job_title6, self.past_job_org_summary6, self.past_job_org_detail6, \
        self.past_job_duration6, self.past_job_location6, \
        self.past_job_description6 = past_job_title6, past_job_org_summary6 \
            , past_job_org_detail6, past_job_duration6, past_job_location6, past_job_description6

        self.highestLevel_universityName, self.highestLevel_degree, self.highestLevel_major, \
        self.highestLevel_endDate, self.highestLevel_detail = highestLevel_universityName, highestLevel_degree \
            , highestLevel_major, highestLevel_endDate, highestLevel_detail

        self.otherLevel_universityName1, self.otherLevel_degree1, self.otherLevel_major1, self.otherLevel_endDate1, \
        self.otherLevel_detail1 = otherLevel_universityName1, otherLevel_degree1, otherLevel_major1 \
            , otherLevel_endDate1, otherLevel_detail1
        self.otherLevel_universityName2, self.otherLevel_degree2, self.otherLevel_major2, self.otherLevel_endDate2, \
        self.otherLevel_detail2 = otherLevel_universityName2, otherLevel_degree2, otherLevel_major2 \
            , otherLevel_endDate2, otherLevel_detail2
        self.otherLevel_universityName3, self.otherLevel_degree3, self.otherLevel_major3, self.otherLevel_endDate3, \
        self.otherLevel_detail3 = otherLevel_universityName3, otherLevel_degree3, otherLevel_major3 \
            , otherLevel_endDate3, otherLevel_detail3
        self.skills = skills
        self.languages = languages

    # def extractandnormalizeworkyear(self):
    def past_work_duration_value(self):
        return [self.past_job_duration1, self.past_job_duration2, self.past_job_duration3, self.past_job_duration4,
                self.past_job_duration5, self.past_job_duration6, self.past_job_duration7, self.past_job_duration8,
                self.past_job_duration9, self.past_job_duration10]

    def getworkdurationvalue(self, past_job_duration1, past_job_duration2, past_job_duration3, past_job_duration4,
                                 past_job_duration5, past_job_duration6, past_job_duration7, past_job_duration8,
                                 past_job_duration9, past_job_duration10):
        self.past_job_duration1 = past_job_duration1
        self.past_job_duration2 = past_job_duration2
        self.past_job_duration3 = past_job_duration3
        self.past_job_duration4 = past_job_duration4
        self.past_job_duration5 = past_job_duration5
        self.past_job_duration6 = past_job_duration6
        self.past_job_duration7 = past_job_duration7
        self.past_job_duration8 = past_job_duration8
        self.past_job_duration9 = past_job_duration9
        self.past_job_duration10 = past_job_duration10

    def return_value_all(self):
        return remove_non_alphapet.remove_non_alpha([
        # self.id,
        # self.name,
        # self.connections,
        self.title,
        self.org_summary,
        self.org_detail,
        # self.duration,
        self.location,
        self.description,
        self.past_job_title1, self.past_job_org_summary1, self.past_job_org_detail1,
        # self.past_job_duration1,
        self.past_job_location1,
        self.past_job_description1,
        self.past_job_title2, self.past_job_org_summary2, self.past_job_org_detail2,
        # self.past_job_duration2,
        self.past_job_location2,
        self.past_job_description2,
        self.past_job_title3, self.past_job_org_summary3, self.past_job_org_detail3,
        # self.past_job_duration3,
        self.past_job_location3,
        self.past_job_description3,
        self.past_job_title4, self.past_job_org_summary4, self.past_job_org_detail4,
        # self.past_job_duration4,
        self.past_job_location4,
        self.past_job_description4,
        self.past_job_title5, self.past_job_org_summary5, self.past_job_org_detail5,
        # self.past_job_duration5,
        self.past_job_location5,
        self.past_job_description5,
        self.past_job_title6, self.past_job_org_summary6, self.past_job_org_detail6,
        # self.past_job_duration6,
        self.past_job_location6,
        self.past_job_description6,

        # self.highestLevel_universityName,
        self.highestLevel_degree, self.highestLevel_major,
        # self.highestLevel_endDate,
        self.highestLevel_detail,

        # self.otherLevel_universityName1,
        self.otherLevel_degree1, self.otherLevel_major1,
        # self.otherLevel_endDate1,
        self.otherLevel_detail1,
        # self.otherLevel_universityName2,
        self.otherLevel_degree2, self.otherLevel_major2,
        # self.otherLevel_endDate2,
        self.otherLevel_detail2,
        # self.otherLevel_universityName3,
        self.otherLevel_degree3, self.otherLevel_major3,
        # self.otherLevel_endDate3,
        self.otherLevel_detail3,
        # self.skills.split(','),
        self.languages]+self.skills.split(','))


    def return_value_work_exp(self):
        return remove_non_alphapet.remove_non_alpha([self.past_job_title1, self.past_job_org_summary1, self.past_job_org_detail1,
        self.past_job_duration1, self.past_job_location1,
        self.past_job_description1,
        self.past_job_title2, self.past_job_org_summary2, self.past_job_org_detail2,
        self.past_job_duration2, self.past_job_location2,
        self.past_job_description2,
        self.past_job_title3, self.past_job_org_summary3, self.past_job_org_detail3,
        self.past_job_duration3, self.past_job_location3,
        self.past_job_description3,
        self.past_job_title4, self.past_job_org_summary4, self.past_job_org_detail4,
        self.past_job_duration4, self.past_job_location4,
        self.past_job_description4,
        self.past_job_title5, self.past_job_org_summary5, self.past_job_org_detail5,
        self.past_job_duration5, self.past_job_location5,
        self.past_job_description5,
        self.past_job_title6, self.past_job_org_summary6, self.past_job_org_detail6,
        self.past_job_duration6, self.past_job_location6,
        self.past_job_description6,
        ])

    def return_value_edu(self):
        return remove_non_alphapet.remove_non_alpha([self.highestLevel_universityName, self.highestLevel_degree, self.highestLevel_major,
        self.highestLevel_endDate, self.highestLevel_detail,

        self.otherLevel_universityName1, self.otherLevel_degree1, self.otherLevel_major1, self.otherLevel_endDate1,
        self.otherLevel_detail1,
        self.otherLevel_universityName2, self.otherLevel_degree2, self.otherLevel_major2, self.otherLevel_endDate2,
        self.otherLevel_detail2,
        self.otherLevel_universityName3, self.otherLevel_degree3, self.otherLevel_major3, self.otherLevel_endDate3,
        self.otherLevel_detail3])

    def return_value_skills(self):
        return remove_non_alphapet.remove_non_alpha([self.languages]+self.skills.split(','))