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
