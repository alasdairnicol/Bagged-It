"""
Script to import all the munros from input.txt

input.txt taken from http://www.smc.org.uk/Munros/MunrosTable.

== Input format ==

Each line in input.txt corresponds to a munro, and is of the form

<number>\t<name>\t<translation>\t<height\t<grid ref>\tO/S

e.g.
M001	Ben Nevis	Possibly from an old Gaelic word meaning venomous	1344	NN 166 712	O/S


"""
from munros.models import Munro, Section

SECTIONS = """\
01,Loch Lomond to Loch Tay
02,Loch Tay to Rannoch Moor
03,Strath Orchy to Loch Leven
04,Loch Linnhe to Loch Ericht
05,Loch Rannoch to Drumochter
06,Glen Garry to Braemar
07,Glen Shee to Mount Keen
08,The Cairngorms
09,Glen Roy to The Monadh Liath
10,Loch Eil to Glen Shiel
11,Glen Affric and Kintail
12,Glen Cannich to Glen Carron
13,Coulin and Torridon
14,Loch Maree to Loch Broom
15,Loch Broom to Easter Ross
16,Coigach to Cape Wrath
17,The Islands""".split("\n")

def create_sections():
    """
    Adds the sections to the database, using data in SECTIONS
    """
    for line in SECTIONS:
        num, name = line.split(",")
        section = Section.objects.create(pk=int(num),
                                         name=name,
                                         description="",
                                         )
        print "Created section %s" % section


def create_munros():
    """
    Adds the munros to the database, using data in input.txt
    """
    f=open('/home/aan/dev/baggedit/baggedit/munros/input.txt','r')
    munros = f.readlines()

    for m in munros:
        data = m.split("\t")
        number = int(data[0][1:]) # M001 -> 1
        munro = Munro.objects.create(pk=number,
                                     name=data[1],
                                     section_id = 1,
                                     translation=data[2],
                                     height=data[3],
                                     summit_grid_ref=data[4],
                                     )
        print "Created munro %s" % munro


MUNROS_BY_SECTION = {
    1: ("M147","M281","M233","M216","M244","M175","M259","M220","M250","M118","M184","M028","M016","M101","M282","M229","M165","M087","M018","M182",),
    2: ("M034","M061","M094","M129","M064","M047","M062","M211","M106","M010","M103","M091","M084","M261","M248","M068","M186","M035","M093","M199","M136","M169","M089","M059","M270","M197",),
    3: ("M172","M156","M198","M196","M237","M031","M063","M023","M263","M201","M110","M207","M050","M145","M045","M212","M254","M149","M107","M137","M188","M226","M090","M065","M143","M055",),
    4: ("M099","M166","M007","M037","M008","M056","M112","M048","M241","M025","M001","M230","M027","M098","M231","M009","M086","M264","M081","M026","M236","M074","M208","M051","M052","M123","M046","M140","M178","M015","M171","M038","M039","M174",),
    5: ("M240","M179","M119","M232","M279","M214","M155",),
    6: ("M126","M227","M124","M088","M066","M192","M180","M148","M102","M278","M221","M181","M032","M079","M245",),
    7: ("M142","M117","M071","M042","M083","M113","M159","M219","M069","M021","M253","M235","M202","M204",),
    8: ("M011","M058","M249","M019","M013","M017","M002","M003","M054","M006","M004","M095","M020","M040","M114","M005","M036","M130",),
    9: ("M251","M080","M283","M225","M127","M271","M030","M260","M076",),
    10: ("M109","M183","M218","M274","M160","M272","M116","M097","M161","M111","M234","M168","M222","M275","M104","M122","M131","M132","M092","M223","M213","M206","M193","M146","M239","M121",),
    11: ("M033","M273","M269","M135","M100","M128","M012","M203","M173","M014","M049","M167","M133","M205","M096","M070","M134","M105","M022","M044","M077","M041",),
    12: ("M029","M067","M224","M152","M153","M163","M125","M255","M078","M060","M139","M082","M024","M151",),
    13: ("M120","M258","M247","M108","M195","M162","M075","M150","M268",),
    14: ("M144","M187","M266","M280","M209","M238","M072","M246","M243","M215","M115","M276","M157","M138","M073","M043","M053","M267","M170",),
    15: ("M210","M057","M085","M176","M257","M177","M262",),
    16: ("M256","M194","M141","M158",),
    17: ("M242","M189","M252","M200","M185","M277","M154","M164","M228","M217","M190","M265","M191",),
}

def set_munros_section():
    """
    Iterates through MUNROS_BY_SECTION, and updates the munro.section
    for each munro in that section.
    """
    for section_id, munros_list in MUNROS_BY_SECTION.iteritems():
        section = Section.objects.get(pk=section_id)
        for munro_id in munros_list:
            munro=Munro.objects.get(pk=int(munro_id[1:]))
            munro.section_id=section
            munro.save()
            print "Added munro %s to section %s" % (munro, section)
