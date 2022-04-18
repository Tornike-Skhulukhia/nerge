try:
    from ..country.get_meta import DATA as countries_data
except Exception:
    from country.get_meta import DATA as countries_data

# delete this words before processing, as spacy seems to think they are parts of person name
INCORRECT_PERSON_LIKE_WORDS_FOR_SPACY = {
    # write most common problematic ones for our cases
    # government/profession
    "chair",
    "chairperson",
    "chairman",
    "pm",
    "gd",
    "unm",
    "fm",
    "vice",
    # Georgian Cities
    "tbilisi",
    "batumi",
    "kutaisi",
    "rustavi",
    "gori",
    "zugdidi",
    "poti",
    "kobuleti",
    "khashuri",
    "samtredia",
    "senaki",
    "zestafoni",
    "marneuli",
    "telavi",
    "akhaltsikhe",
    "ozurgeti",
    "kaspi",
    "chiatura",
    "tsqaltubo",
    "sagarejo",
    "gardabani",
    "borjomi",
    "tkibuli",
    "khoni",
    "bolnisi",
    "akhalkalaki",
    "gurjaani",
    "mtskheta",
    "kvareli",
    "akhmeta",
    "kareli",
    "lanchkhuti",
    "tsalenjikha",
    "dusheti",
    "sachkhere",
    "dedoplistsqaro",
    "lagodekhi",
    "ninotsminda",
    "abasha",
    "tsnori",
    "terjola",
    "martvili",
    "jvari",
    "khobi",
    "vani",
    "baghdati",
    "vale",
    "tetritsqaro",
    "tsalka",
    "dmanisi",
    "oni",
    "ambrolauri",
    "sighnaghi",
    "tsageri",
    "sukhumi",
    "tkvarcheli",
    "ochamchire",
    "gali",
    "gudauta",
    "pitsunda",
    "gulripshi",
    "gagra",
    "new athos",
    # world cities
    "shanghai",
    "beijing",
    "karachi",
    "istanbul",
    "dhaka",
    "tokyo",
    "moscow",
    "manila",
    "tianjin",
    "mumbai",
    "bombay",
    "sao paulo",
    "shenzhen",
    "guangzhou",
    "delhi",
    "wuhan",
    "lahore",
    "seoul",
    "chengdu",
    "kinshasa",
    "lima",
    "jakarta",
    "cairo",
    "mexico",
    "tehran",
    "baghdad",
    "xian",
    "london",
    "new york",
    "nanjing",
    "bangalore",
    "ho chi minh",
    "bangkok",
    "chongquin",
    "bogota",
    "lagos",
    "riyadh",
    "hong kong",
    "chennai",
    "hangzhou",
    "hyderabad",
    "rio de janeiro",
    "zhengzhou",
    "shenyang",
    "qingdao",
    "santiago",
    "dalian",
    "singapore",
    "ahmadabad",
    "suzhou",
    "st petersburg",
    "harbin",
    "ankara",
    "khartoum",
    "yangon",
    "casablanca",
    "sydney",
    "jinan",
    "melbourne",
    "changsha",
    "kolkata",
    "fuzhou",
    "surat",
    "abidjan",
    "dar es salaam",
    "shiziahuang",
    "jeddah",
    "faisalabad",
    "nanning",
    "alexandria",
    "amman",
    "los angeles",
    "kunming",
    "changchun",
    "yokohama",
    "kabul",
    "berlin",
    "giza",
    "urumqi",
    "wuxi",
    "busan",
    "guayaquil",
    "hanoi",
    "hyderabad",
    "addis ababa",
    "algiers",
    "kano",
    "mashhad",
    "hefei",
    "changzhou",
    "taiyuan",
    "rawalpindi",
    "tangshan",
    "madrid",
    "nairobi",
    "zibo",
    "pune",
    "ibadan",
    "jaipur",
    "guiyang",
    "incheon",
    "brasilia",
    "tshwane",
    "pretoria",
    "kanpur",
    "salvador",
    "buenos aires",
    "kiev",
    "rome",
    "surabaya",
    "izmir",
    "lucknow",
    "basrah",
    "toronto",
    "gujranwala",
    "chicago",
    "taipei",
    "quito",
    "osaka",
    "xuzhou",
    "fortaleza",
    "chittagong",
    "pyongyang",
    "bandung",
    "kaohsiung",
    "yaounde",
    "daegu",
    "taichung",
    "belo horizonte",
    "puebla",
    "douala",
    "medellin",
    "nagpur",
    "cali",
    "omdurman",
    "nanchang",
    "brisbane",
    "bursa",
    "tashkent",
    "houston",
    "nagoya",
    "mogadishu",
    "isfahen",
    "paris",
    "accra",
    "managua",
    "kowloon",
    "lanzhou",
    "baku",
    "guatamala",
    "luanda",
    "bucharest",
    # roman numeric
    "I",
    # other
    "case",
    "visit",
    "grant",
    "covid",
}

# also remove countries
INCORRECT_PERSON_LIKE_WORDS_FOR_SPACY.update(
    {i["name_en"].lower() for i in countries_data.values()}
)


# add plural forms
INCORRECT_PERSON_LIKE_WORDS_FOR_SPACY.update(
    {f"{i}s" for i in INCORRECT_PERSON_LIKE_WORDS_FOR_SPACY}
)