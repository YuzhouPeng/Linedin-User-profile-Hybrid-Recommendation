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
                 past_job_title7, past_job_org_summary7, past_job_org_detail7, past_job_duration7, past_job_location7,
                 past_job_description7,
                 past_job_title8, past_job_org_summary8, past_job_org_detail8, past_job_duration8, past_job_location8,
                 past_job_description8,
                 past_job_title9, past_job_org_summary9, past_job_org_detail9, past_job_duration9, past_job_location9,
                 past_job_description9,
                 past_job_title10, past_job_org_summary10, past_job_org_detail10, past_job_duration10,
                 past_job_location10,
                 past_job_description10,
                 highestLevel_universityName, highestLevel_degree, highestLevel_major,
                 highestLevel_endDate, highestLevel_detail,
                 otherLevel_universityName1, otherLevel_degree1, otherLevel_major1, otherLevel_endDate1,
                 otherLevel_detail1,
                 otherLevel_universityName2, otherLevel_degree2, otherLevel_major2, otherLevel_endDate2,
                 otherLevel_detail2,
                 otherLevel_universityName3, otherLevel_degree3, otherLevel_major3, otherLevel_endDate3,
                 otherLevel_detail3,
                 otherLevel_universityName4, otherLevel_degree4, otherLevel_major4, otherLevel_endDate4,
                 otherLevel_detail4,
                 otherLevel_universityName5, otherLevel_degree5, otherLevel_major5, otherLevel_endDate5,
                 otherLevel_detail5,
                 otherLevel_universityName6, otherLevel_degree6, otherLevel_major6, otherLevel_endDate6,
                 otherLevel_detail6,
                 otherLevel_universityName7, otherLevel_degree7, otherLevel_major7, otherLevel_endDate7,
                 otherLevel_detail7,
                 skills, languages, associations):
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
        self.past_job_title7, self.past_job_org_summary7, self.past_job_org_detail7, \
        self.past_job_duration7, self.past_job_location7, \
        self.past_job_description7 = past_job_title7, past_job_org_summary7 \
            , past_job_org_detail7, past_job_duration7, past_job_location7, past_job_description7
        self.past_job_title8, self.past_job_org_summary8, self.past_job_org_detail8, \
        self.past_job_duration8, self.past_job_location8, \
        self.past_job_description8 = past_job_title8, past_job_org_summary8 \
            , past_job_org_detail8, past_job_duration8, past_job_location8, past_job_description8
        self.past_job_title9, self.past_job_org_summary9, self.past_job_org_detail9, \
        self.past_job_duration9, self.past_job_location9, \
        self.past_job_description9 = past_job_title9, past_job_org_summary9 \
            , past_job_org_detail9, past_job_duration9, past_job_location9, past_job_description9
        self.past_job_title10, self.past_job_org_summary10, self.past_job_org_detail10, \
        self.past_job_duration10, self.past_job_location10, \
        self.past_job_description10 = past_job_title10, past_job_org_summary10 \
            , past_job_org_detail10, past_job_duration10, past_job_location10, past_job_description10

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
        self.otherLevel_universityName4, self.otherLevel_degree4, self.otherLevel_major4, self.otherLevel_endDate4, \
        self.otherLevel_detail4 = otherLevel_universityName4, otherLevel_degree4, otherLevel_major4 \
            , otherLevel_endDate4, otherLevel_detail4
        self.otherLevel_universityName5, self.otherLevel_degree5, self.otherLevel_major5, self.otherLevel_endDate5, \
        self.otherLevel_detail5 = otherLevel_universityName5, otherLevel_degree5, otherLevel_major5 \
            , otherLevel_endDate5, otherLevel_detail5
        self.otherLevel_universityName6, self.otherLevel_degree6, self.otherLevel_major6, self.otherLevel_endDate6, \
        self.otherLevel_detail6 = otherLevel_universityName6, otherLevel_degree6, otherLevel_major6 \
            , otherLevel_endDate6, otherLevel_detail6
        self.otherLevel_universityName7, self.otherLevel_degree7, self.otherLevel_major7, self.otherLevel_endDate7, \
        self.otherLevel_detail7 = otherLevel_universityName7, otherLevel_degree7, otherLevel_major7 \
            , otherLevel_endDate7, otherLevel_detail7
        self.skills = skills
        self.languages = languages
        self.associations = associations

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

    def return_value(self):
        return [self.id,
        self.name,
        # self.connections,
        self.title,
        self.org_summary,
        # self.org_detail,
        # self.duration,
        # self.location,
        self.description,
        self.past_job_title1, self.past_job_org_summary1, self.past_job_org_detail1,
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
        self.past_job_title7, self.past_job_org_summary7, self.past_job_org_detail7,
        self.past_job_duration7, self.past_job_location7,
        self.past_job_description7,
        self.past_job_title8, self.past_job_org_summary8, self.past_job_org_detail8,
        self.past_job_duration8, self.past_job_location8,
        self.past_job_description8,
        self.past_job_title9, self.past_job_org_summary9, self.past_job_org_detail9,
        self.past_job_duration9, self.past_job_location9,
        self.past_job_description9,
        self.past_job_title10, self.past_job_org_summary10, self.past_job_org_detail10,
        self.past_job_duration10, self.past_job_location10,
        self.past_job_description10,

        self.highestLevel_universityName, self.highestLevel_degree, self.highestLevel_major,
        self.highestLevel_endDate, self.highestLevel_detail,

        self.otherLevel_universityName1, self.otherLevel_degree1, self.otherLevel_major1, self.otherLevel_endDate1,
        self.otherLevel_detail1,
        self.otherLevel_universityName2, self.otherLevel_degree2, self.otherLevel_major2, self.otherLevel_endDate2,
        self.otherLevel_detail2,
        self.otherLevel_universityName3, self.otherLevel_degree3, self.otherLevel_major3, self.otherLevel_endDate3,
        self.otherLevel_detail3,
        self.otherLevel_universityName4, self.otherLevel_degree4, self.otherLevel_major4, self.otherLevel_endDate4,
        self.otherLevel_detail4,
        self.otherLevel_universityName5, self.otherLevel_degree5, self.otherLevel_major5, self.otherLevel_endDate5,
        self.otherLevel_detail5,
        self.otherLevel_universityName6, self.otherLevel_degree6, self.otherLevel_major6, self.otherLevel_endDate6,
        self.otherLevel_detail6,
        self.otherLevel_universityName7, self.otherLevel_degree7, self.otherLevel_major7, self.otherLevel_endDate7,
        self.otherLevel_detail7,
        self.skills,
        self.languages,
        self.associations]
