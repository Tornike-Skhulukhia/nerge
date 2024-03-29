from country.extract import extract_countries


def test_1():
    text = "იყო და არა იყო რა"
    answer = []

    assert sorted(answer) == extract_countries(text)


def test_2():
    text = "ქართულ სახელმწიფოს 4 მოსაზღვრე ქვეყანა ყავს: რუსეთი, თურქეთი, სომხეთი და აზერბაიჯანი"
    answer = ["GE", "RU", "TR", "AM", "AZ"]

    assert sorted(answer) == extract_countries(text)


def test_3():
    text = "საქართველოს ესაზღვრებიან რუსი, თურქი, სომეხი და აზერბაიჯანელი მეზობლები"
    answer = ["GE", "RU", "TR", "AM", "AZ"]

    assert sorted(answer) == extract_countries(text)


def test_4():
    text = """
        საქართველომ 2021 წლის 11 თვეში 1.4 მლნ დოლარის 145 ტონა ფეიერვერკები, სასიგნალო შუშხუნები, წვიმის რაკეტები
        და სხვა პიროტექნიკური ნაწარმი შეიძინა. ოფიციალური სტატისტიკის მიხედვით, 2020 წლის ამავე პერიოდთან შედარებით
        გასული წლის იანვარ-ნოემბერში საქართველომ 59.7%-ით ნაკლები ღირებულების საქონელი შეიძინა, იმპორტირებული
        სხვადასხვა პიროტექნიკური ნაწარმის მოცულობა კი პანდემიურ წელთან შედარებით 84.5%-ით არის შემცირებული.
        აღსანიშნია, რომ 2019 წელთან შედარებით აღნიშნული საქონლის საიმპორტო მოცულობების მნიშვნელოვნი კლევა ფიქსირდება
        (2019 წელი - 5.9 მლნ დოლარი, 1 481 ტონა).
        2021 წლის 11 თვეში, წინა წელთან შედარებით ფეიერვერკების, სასიგნალო შუშხუნების, წვიმის რაკეტების და სხვა პიროტექნიკური
        ნაწარმის იმპორტი ჩინეთიდან, რომელიც წლების განმავლობაში ერთ-ერთი მთავარი საიმპორტო ბაზარი იყო, 83%-ით შემცირდა.
        საიმპორტო ქვეყნები კი ასეთია:
            1. მონტენეგრო - 501.8 ათასი აშშ დოლარი;
            2. ბულგარეთი - 393.6 ათასი აშშ დოლარი;
            3. ჩინეთი - 278.4 ათასი აშშ დოლარი;
            4. პოლონეთი - 169.8 ათასი აშშ დოლარი;
            5. გერმანია - 15.2 ათასი აშშ დოლარი;
            6. თურქეთი - 11.2 ათასი აშშ დოლარი.
    """

    answer = ["GE", "CN", "ME", "BG", "PL", "DE", "TR"]

    assert sorted(answer) == extract_countries(text)


def test_5():
    text = """საპროტესტო აქციების ფონზე "კასპის" გუნდი ყაზახეთის მთავრობას ეხმარება - მიხეილ ლომთაძის პოსტი"""

    answer = ["KZ"]
    assert sorted(answer) == extract_countries(text)


def test_6():
    text = """
        საქართველოს პრეზიდენტი შალვა ნათელაშვილი შეერთებული შტატების
        პრეზიდენტს საპრეზიდენტო სასახლეში დღეს უმასპინძლებს. შეხვედრას ასევე დაესწრებიან რუსი,
        ჩინელი, ფრანგი და დიდი ბრიტანელი დიპლომატები. შეხვედრის შემდეგ გაიმართება ამხანაგური
        საფეხბურთო მატჩი ბრაზილია-გერმანია, რომელსაც კორონავირუსის გავრცელების პრევენციის
        მიზნით მაყურებელი არ დაესწრება.
    """

    answer = ["BR", "CN", "DE", "FR", "GB", "GE", "RU", "US"]

    assert sorted(answer) == extract_countries(text)


def test_7():
    text = """
        ავღანეთიდან სასწრაფო ევაკუაციაში საქართველო ჩაერთო - თბილისის აეროპორტში ნატოს
        სამხედრო-სატრანსპორტო თვითმფრინავები განთავსდა
    """

    answer = ["AF", "GE"]
    assert sorted(answer) == extract_countries(text)


def test_7():
    text = """
       დღეს, როდესაც ავღანეთში განვითარებულმა ტრაგიკულმა მოვლენებმა დაგვაყენა მასშტაბური
       ჰუმანიტარული კრიზისის საფრთხის წინაშე, საქართველო კვლავ დგას მისი პარტნიორების
       გვერდით და აქტიურად არის ჩართული ჰუმანიტარული და საევაკუაციო პროცესების მართვაში.
       თბილისის აეროპორტში განლაგდა ნატო-ს სამხედრო-სატრანსპორტო გადაზიდვების
       ორგანიზაციის სამხედრო-სატვირთო თვითმფრინავები, რომლებიც ყოველდღიურად ასრულებენ
       ფრენებს ქაბულის მიმართულებით. ხოლო, ქაბულიდან თბილისის აეროპორტში ევაკუირებული
       მგზავრების გადაყვანა ხორციელდება სხვადასხვა ჩარტერული რეისების საშუალებით
       (დღეისთვის განხორციელებულია 2 000-მდე მგზავრის ევაკუაცია). თბილისის საერთაშორისო
       აეროპორტში და აეროპორტთან არსებული საქართველოს თავდაცვის ძალების სამხედრო ბაზაზე
       ჩამოყალიბდა რეგიონული სატრანზიტო ჰაბი, რომლის ფუნქციონირებაშიც მონაწილეობს
       ქართველი, ნორვეგიელი, შვედი და ნატო-ს წევრი სხვა ქვეყნების სამხედრო და
       სამოქალაქო პერსონალი. ასევე, სამხედრო ბაზის ტერიტორიაზე ნორვეგიის შეიარაღებული
       ძალების მიერ მოეწყო სატრანზიტო სამედიცინო დახმარების პუნქტი, რომელიც,
       საჭიროების შემთხვევაში, გამოყენებული იქნება ქაბულში არსებული ნორვეგიული
       სამხედრო ჰოსპიტლის ევაკუაციისას.

    """

    answer = ["AF", "GE", "NO", "SE"]
    assert sorted(answer) == extract_countries(text)


def test_8():
    text = """
        გასულ წელს ყველაზე დიდი მოცულობით კოჭა, ზაფრანა, ურცი, დაფნის ფოთოლი, კარი და სხვა
        სანელებლები საქართველოდან რუსეთში, ჩინეთსა და უკრაინაში გაიყიდა. აღსანიშნია ისიც,
        რომ 2021 წელს აშშ ტოპ საექსპორტო ბაზრებს შორის მოხვდა.

        TOP-10 საექსპორტო ბაზრის ჩამონათვალი კი ასეთია:

        1. რუსეთი - 4.2 მლნ დოლარი, 1 730 ტონა;
        2. ჩინეთი - 3.1 მლნ დოლარი, 1 627 ტონა;
        3. უკრაინა - 1.2 მლნ დოლარი, 574 ტონა;
        4. აშშ - 1.1 მლნ დოლარი, 235 ტონა;
        5. ფილიპინები - 206.5 ათასი დოლარი, 99 ტონა;
        6. ყაზახეთი - 189.5 ათასი დოლარი, 139 ტონა;
        7. სომხეთი - 170.8 ათასი დოლარი, 73 ტონა;
        8. უზბეკეთი - 153.4 ათასი დოლარი, 239 ტონა;
        9. მოლდოვა - 116 ათასი დოლარი, 51 ტონა;
        10. ესპანეთი - 99 ათასი დოლარი, 27 ტონა;

        გარდა ამისა, მცირე მოცულობებით სანელებლების ექსპორტი ბულგარეთში, ისრაელში, ნიგერიაში,
        ბელარუსში, თურქმენეთში, ლატვიაში, პოლონეთში, ტაჯიკეთში, ინდოეთში, ჩეხეთში,
        ყირგიზეთში, თურქეთში, გერმანიაში, საფრანგეთსა და სხვა ქვეყნებში განხორციელდა.
    """

    answer = [
        "GE",
        "RU",
        "CN",
        "UA",
        "US",
        "PH",
        "KZ",
        "AM",
        "UZ",
        "MD",
        "ES",
        "BG",
        "IL",
        "NG",
        "BY",
        "TM",
        "LV",
        "PL",
        "TJ",
        "IN",
        "CZ",
        "KG",
        "TR",
        "DE",
        "FR",
    ]

    assert sorted(answer) == extract_countries(text)


def test_9():
    text = """ქურდობა სენაკში - არსებული ინფორმაციით, გაქურდულია სახლი, სადაც სარემონტო სამუშაოებზე დასაქმებული მუშები ცხოვრობდნენ. შემთხვევა 2 დღის წინ, ღამის საათებში მოხდა. წაღებულია ელექტროლეიბები, გამათბობლები და სარემონტო სამუშაოებისთვის საჭირო ძვირადღირებული ხელსაწყოები. მუშებს ლეიბები და გამათბობლები იმ საავადმყოფომ ათხოვა დროებითი საცხოვრებლისთვის, რომელსაც ისინი არემონტებდნენ. მუშები ვარაუდობენ, რომ ქურდები სავარაუდოდ ავტომანქანით გადაადგილდებოდნენ, რადგან ნაქურდალი ნივთების რაოდენობიდან და მოცულობიდან გამომდინარე, ხელით მათი წაღება გაუჭირდებოდათ. მომხდარზე გამოძიება სსკ-ის 117-ე, ქურდობის მუხლით მიმდინარეობს. ავტორი: ემა გოგოხია."""

    result = []

    assert sorted(result) == extract_countries(text)


def test_10():
    text = """ბადრაგმა ფიზიკური და სიტყვიერი შეურაცხყოფა მიაყენა ადვოკატს და სხვა ბადრაგებმა გაარიდეს დანაშაულის (სწორედ, დანაშაულის) ჩადენის ადგილს."""

    result = []

    assert sorted(result) == extract_countries(text)


def test_11():
    text = """ბაგარები — არაბული ტომები, რომელთა რაოდენობაც ჯამში დაახლოებით 1 მილიონს შეადგენს. მათი უმეტესობა ცხოვრობს ჩადიში და სუდანის დარფურის რეგიონში (ძირითადად ფურები, ნუბა და ფულბეები). ისინი პერიოდულად მიგრირებენ სამხრეთ სუდანსა და მიმდებარე რეგიონებში. დასავლეთი ბაჰრ-ელ-ღაზალის ჩრდილოეთ ნაწილი არის ბაგარების სამხრეთ სუდანში გადმოსახლების ტრადიციული არეალი. მათი დასახელების არაბულიდან პირდაპირი თარგმანი არის მეძროხე, ისინი საუბრობენ ჩადის არაბულზე."""

    result = ["TD", "SD", "SS"]

    assert sorted(result) == extract_countries(text)


def test_11():
    text = """ჩვენი მიზანია, საქართველოს მოსახლეს შეეძლოს მოსვლა, ამიტომ ვფიქრობთ, საშუალო საფასო სეგმენტზე იქნება მორგებული", - განაცხადა bmg-სთან საუბრისას ტოგონიძემ. """

    result = ["GE"]

    assert sorted(result) == extract_countries(text)


def test_12():
    text = """
    მთავრობის გადაწყვეტილებით, ყველას, ვინც მოიხმარს 200 კილოვატზე ნაკლებ ელექტროენერგიას და 200 კუბურ მეტრზე ნაკლებ ბუნებრივ აირს, კომუნალური გადასახადი სამი თვის განმავლობაში სრულად დაუფინანსდება 
    """

    result = []

    assert sorted(result) == extract_countries(text)


def test_13():
    text = """
    ფილიპინელი ხალხი
    """

    result = ["PH"]

    assert sorted(result) == extract_countries(text)
