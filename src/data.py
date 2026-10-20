# Reference data for list pages. Sources noted per list.

# UN member states (193), grouped by UN M49 region. Source: UN Statistics Division, M49 standard.
COUNTRIES = {
"Africa": ["Algeria","Angola","Benin","Botswana","Burkina Faso","Burundi","Cabo Verde","Cameroon","Central African Republic","Chad","Comoros","Congo","Côte d'Ivoire","Democratic Republic of the Congo","Djibouti","Egypt","Equatorial Guinea","Eritrea","Eswatini","Ethiopia","Gabon","Gambia","Ghana","Guinea","Guinea-Bissau","Kenya","Lesotho","Liberia","Libya","Madagascar","Malawi","Mali","Mauritania","Mauritius","Morocco","Mozambique","Namibia","Niger","Nigeria","Rwanda","São Tomé and Príncipe","Senegal","Seychelles","Sierra Leone","Somalia","South Africa","South Sudan","Sudan","Tanzania","Togo","Tunisia","Uganda","Zambia","Zimbabwe"],
"Americas": ["Antigua and Barbuda","Argentina","Bahamas","Barbados","Belize","Bolivia","Brazil","Canada","Chile","Colombia","Costa Rica","Cuba","Dominica","Dominican Republic","Ecuador","El Salvador","Grenada","Guatemala","Guyana","Haiti","Honduras","Jamaica","Mexico","Nicaragua","Panama","Paraguay","Peru","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Suriname","Trinidad and Tobago","United States","Uruguay","Venezuela"],
"Asia": ["Afghanistan","Armenia","Azerbaijan","Bahrain","Bangladesh","Bhutan","Brunei","Cambodia","China","Cyprus","Georgia","India","Indonesia","Iran","Iraq","Israel","Japan","Jordan","Kazakhstan","Kuwait","Kyrgyzstan","Laos","Lebanon","Malaysia","Maldives","Mongolia","Myanmar","Nepal","North Korea","Oman","Pakistan","Philippines","Qatar","Saudi Arabia","Singapore","South Korea","Sri Lanka","Syria","Tajikistan","Thailand","Timor-Leste","Turkey","Turkmenistan","United Arab Emirates","Uzbekistan","Vietnam","Yemen"],
"Europe": ["Albania","Andorra","Austria","Belarus","Belgium","Bosnia and Herzegovina","Bulgaria","Croatia","Czechia","Denmark","Estonia","Finland","France","Germany","Greece","Hungary","Iceland","Ireland","Italy","Latvia","Liechtenstein","Lithuania","Luxembourg","Malta","Moldova","Monaco","Montenegro","Netherlands","North Macedonia","Norway","Poland","Portugal","Romania","Russia","San Marino","Serbia","Slovakia","Slovenia","Spain","Sweden","Switzerland","Ukraine","United Kingdom"],
"Oceania": ["Australia","Fiji","Kiribati","Marshall Islands","Micronesia","Nauru","New Zealand","Palau","Papua New Guinea","Samoa","Solomon Islands","Tonga","Tuvalu","Vanuatu"],
}

# US states by US Census Bureau region.
STATES = {
"Northeast": ["Connecticut","Maine","Massachusetts","New Hampshire","New Jersey","New York","Pennsylvania","Rhode Island","Vermont"],
"Midwest": ["Illinois","Indiana","Iowa","Kansas","Michigan","Minnesota","Missouri","Nebraska","North Dakota","Ohio","South Dakota","Wisconsin"],
"South": ["Alabama","Arkansas","Delaware","Florida","Georgia","Kentucky","Louisiana","Maryland","Mississippi","North Carolina","Oklahoma","South Carolina","Tennessee","Texas","Virginia","West Virginia"],
"West": ["Alaska","Arizona","California","Colorado","Hawaii","Idaho","Montana","Nevada","New Mexico","Oregon","Utah","Washington","Wyoming"],
}

NFL = {
"AFC East": ["Buffalo Bills","Miami Dolphins","New England Patriots","New York Jets"],
"AFC North": ["Baltimore Ravens","Cincinnati Bengals","Cleveland Browns","Pittsburgh Steelers"],
"AFC South": ["Houston Texans","Indianapolis Colts","Jacksonville Jaguars","Tennessee Titans"],
"AFC West": ["Denver Broncos","Kansas City Chiefs","Las Vegas Raiders","Los Angeles Chargers"],
"NFC East": ["Dallas Cowboys","New York Giants","Philadelphia Eagles","Washington Commanders"],
"NFC North": ["Chicago Bears","Detroit Lions","Green Bay Packers","Minnesota Vikings"],
"NFC South": ["Atlanta Falcons","Carolina Panthers","New Orleans Saints","Tampa Bay Buccaneers"],
"NFC West": ["Arizona Cardinals","Los Angeles Rams","San Francisco 49ers","Seattle Seahawks"],
}

NBA = {
"Atlantic": ["Boston Celtics","Brooklyn Nets","New York Knicks","Philadelphia 76ers","Toronto Raptors"],
"Central": ["Chicago Bulls","Cleveland Cavaliers","Detroit Pistons","Indiana Pacers","Milwaukee Bucks"],
"Southeast": ["Atlanta Hawks","Charlotte Hornets","Miami Heat","Orlando Magic","Washington Wizards"],
"Northwest": ["Denver Nuggets","Minnesota Timberwolves","Oklahoma City Thunder","Portland Trail Blazers","Utah Jazz"],
"Pacific": ["Golden State Warriors","LA Clippers","Los Angeles Lakers","Phoenix Suns","Sacramento Kings"],
"Southwest": ["Dallas Mavericks","Houston Rockets","Memphis Grizzlies","New Orleans Pelicans","San Antonio Spurs"],
}
NBA_CONF = {"Eastern": ["Atlantic","Central","Southeast"], "Western": ["Northwest","Pacific","Southwest"]}

MLB = {
"AL East": ["Baltimore Orioles","Boston Red Sox","New York Yankees","Tampa Bay Rays","Toronto Blue Jays"],
"AL Central": ["Chicago White Sox","Cleveland Guardians","Detroit Tigers","Kansas City Royals","Minnesota Twins"],
"AL West": ["Athletics","Houston Astros","Los Angeles Angels","Seattle Mariners","Texas Rangers"],
"NL East": ["Atlanta Braves","Miami Marlins","New York Mets","Philadelphia Phillies","Washington Nationals"],
"NL Central": ["Chicago Cubs","Cincinnati Reds","Milwaukee Brewers","Pittsburgh Pirates","St. Louis Cardinals"],
"NL West": ["Arizona Diamondbacks","Colorado Rockies","Los Angeles Dodgers","San Diego Padres","San Francisco Giants"],
}

# Common English-language first names and surnames (illustrative lists for a fun generator, not a census sample).
NAMES = {
"female": ["Olivia","Emma","Charlotte","Amelia","Sophia","Mia","Isabella","Ava","Evelyn","Luna","Harper","Sofia","Camila","Eleanor","Elizabeth","Violet","Scarlett","Emily","Hazel","Lily","Gianna","Aurora","Penelope","Aria","Nora","Chloe","Ellie","Mila","Avery","Layla","Abigail","Ella","Isla","Eliana","Nova","Madison","Zoe","Ivy","Grace","Lucy","Willow","Emilia","Riley","Naomi","Victoria","Stella","Elena","Hannah","Valentina","Maya","Zoey","Delilah","Leah","Lainey","Lillian","Paisley","Genesis","Madelyn","Sadie","Sophie","Ayesha","Fatima","Zara","Sara","Amira","Aaliyah","Priya","Ananya","Mei","Yuna"],
"male": ["Liam","Noah","Oliver","James","Elijah","Mateo","Theodore","Henry","Lucas","William","Benjamin","Levi","Sebastian","Jack","Ezra","Michael","Daniel","Leo","Owen","Samuel","Hudson","Alexander","Asher","Luca","Ethan","John","David","Jackson","Joseph","Mason","Luke","Matthew","Julian","Dylan","Elias","Jacob","Maverick","Gabriel","Logan","Aiden","Thomas","Isaac","Miles","Grayson","Santiago","Anthony","Wyatt","Carter","Jayden","Ezekiel","Caleb","Cooper","Josiah","Charles","Christopher","Isaiah","Nolan","Cameron","Nathan","Adam","Ali","Omar","Hamza","Bilal","Yusuf","Ibrahim","Arjun","Rohan","Kenji","Wei"],
"last": ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez","Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin","Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson","Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores","Green","Adams","Nelson","Baker","Hall","Rivera","Campbell","Mitchell","Carter","Roberts","Gomez","Phillips","Evans","Turner","Diaz","Parker","Cruz","Edwards","Collins","Reyes","Stewart","Morris","Morales","Murphy","Cook","Rogers","Gutierrez","Ortiz","Morgan","Cooper","Peterson","Bailey","Reed","Kelly","Howard","Khan","Ahmed","Patel","Singh","Chen","Wang","Kim","Tanaka","Silva","Rossi","Müller"],
}

def flat(d): return [x for v in d.values() for x in v]
assert len(flat(COUNTRIES)) == 193 and len(set(flat(COUNTRIES))) == 193, len(flat(COUNTRIES))
assert len(flat(STATES)) == 50 and len(set(flat(STATES))) == 50
assert len(flat(NFL)) == 32 and len(flat(NBA)) == 30 and len(flat(MLB)) == 30
