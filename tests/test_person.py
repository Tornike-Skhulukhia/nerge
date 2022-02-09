from person.extract import extract_persons


def test_1():
    text = """
        საპროტესტო აქციების ფონზე "კასპის" გუნდი ყაზახეთის მთავრობას
        ეხმარება - მიხეილ ლომთაძის პოსტი"""

    answer = ["მიხეილ ლომთაძე"]

    assert sorted(answer) == extract_persons(text)


def test_2():
    text = """  
        ექსპრეზიდენტი მიხეილ სააკაშვილი რუსთავის მე-12 პენიტენციური დაწესებულებიდან წერილს აქვეყნებს, 
        რომელშიც ექსპრეზიდენტი პირველად საუბრობს თავის უმცროს გოგონაზე - ელის მარია სააკაშვილზე, 
        მისი და სოფო ნიჟარაძის საერთო შვილზე. 

        "მოგესალმებით რუსთავის ციხიდან, ფიზიკურად დასუსტებული, მაგრამ მორალურად მხნე!
        სამშობლოს თავისუფლებისა და ჩვენი ხალხის ღირსეული მომავლისთვის ბრძოლა გრძელდება! თუმცა, დღეს მინდა მიმავალი 
        წლის მთელი სიმძიმე გვერდით გადავდო. 31 დეკემბერი განსხვავებული დღეა. დღე, რომელიც ყველას გვაერთიანებს და ერთნაირად
        გვიყვარს დიდსა თუ პატარას. ის მხოლოდ საუკეთესო მოგონებებსა და კეთილ სურვილებს აცოცხლებს. ამიტომაც, მინდა მოგილოცოთ
        განურჩევლად ყველას, რადგან ეს დღე ყველასია - იწყება ახალი წელი და ჩნდება ახალი შანსი შეცვალო, 
        გააუმჯობესო, გააკეთილშობილო! მიდის ძველი წელი და გეძლევა შანსი, რომ განვლილ წელში დატოვო ყველაფერი ის, რაც აქამდე არ ან ცუდად
         გამოგდიოდა! წარსულში დატოვო მტრობა, შუღლი, დაპირისპირება - ის, რაც განგრევს შიგნიდან და ანგრევს გარეთ შენს ქვეყანას.
        ყველას გისურვებთ, ახალი 2022 წელი ბედნიერების მომტანი ყოფილიყოს პირადად თქვენთვის და თქვენი სამშობლოსთვის!
        ეს პირველი ახალი წელია, რომელსაც ციხეში ვხვდები, მაგრამ შევეცადე ოპტიმიზმი მაინც არ დამეკარგა და ამაშიც მეპოვნა 
        სიკეთის მარცვალი. დიახ, სამაგიეროდ, წელს პირველი წელია, როდესაც ტელევიზორის ეკრანიდან თავის დედიკოსთან ერთად სცენიდან 
        მოგვესალმება "მთავარი არხის" საახალწლო კონცერტის ყველაზე პატარა მონაწილე, ელის მარია სააკაშვილი. ჩემი ყველაზე საყვარელი 
        გოგო და ყველაზე უმცროსი შვილი. ბედნიერი ვარ, რომ ასეთი შესაძლებლობა მაქვს და ჩემი ახალი წელი სხვებისგან გამორჩეულია არა 
        ციხის კედლებით, არამედ ჩემი საყვარელი გოგოს სატელევიზიო დებიუტით. 
        და კვლავ, გილოცავთ ახალ წელს და გისურვებთ ყოველივე საუკეთესოს. 2022 წელს აუცილებლად უნდა შევცვალოთ ყველაფერი ისე, რომ 
        ჩვენი შვილები უფრო ლაღები და ბედნიერები გახდნენ! გილოცავთ! მრავალს დაესწარით!,"- წერს სააკაშვილი. 
    """

    answer = ["სოფო ნიჟარაძე", "ელის მარია სააკაშვილი", "მიხეილ სააკაშვილი"]

    assert sorted(answer) == extract_persons(text)


def test_3():
    text = """  
       "ომიკრონი" შეიძლება იყოს გვირაბის ბოლოს სინათლე, მაგრამ არ დაგვავიწყდეს ჯერ მხოლოდ გვირაბის შესასვლელში ვართ - ბიძინა კულუმბეგოვი
    """

    answer = ["ბიძინა კულუმბეგოვი"]

    assert sorted(answer) == extract_persons(text)


def test_4():
    text = """  
       60-ზე მეტი, მსოფლიოს სხვადასხვა ქვეყნის, კორპორაციების ხელმძღვანელები, ბიზნესმენები და საქმიანი წრეების წარმომადგენლები ხაზარაძე,
       ჯაფარიძე, წერეთლის ბოლო სასამართლო პროცესის წინ, მამუკა ხაზარაძის მხარდამჭერ წერილს აქვეყნებენ. ინფორმაციას ამის შესახებ "ლელო 
       საქართველო" ავრცელებს. 
       
        მიმართვაში ხელმომწერები ხაზს უსვამენ, მამუკა ხაზარაძის წვლილს, საქართველოს განვითარებასა და საერთაშორისო ბიზნეს წრეებში ქვეყნის 
        ცნობადობის გაზრდაში და იმედს გამოთქვამენ, რომ ამ ყველაფერს საქართველოს სასამართლო გაითვალისწინებს და გამამართლებელ განაჩენს გამოიტანს.

       "მამუკამ მთელი მისი ცხოვრება საქართველოს აღმშენებლობას მიუძღვნა. მისმა აშკარა ძალისხმევამ და წარმატებამ, გააუმჯობესა მრავალი ინდუსტრია,
        მათ შორის საბანკო სისტემა და მთელი ქვეყნის ეკონომიკა. ჩვენ, ჰარვარდის ბიზნეს სკოლის კუსრდამთავრებულები და მამუკა ხაზარაძის მეგობრები,
         „OPM29 2000“ - ვიცნობთ რა მამუკას უკვე 20 წელზე მეტია, მხარდაჭერას ვუცხადებთ მას, რადგან ვიცით რა მისი პატრიოტიზმი, პატიოსნება და 
         ერთგულება ქართველი ხალხის მიმართ.
        მამუკა ხაზარაძე ჩვენი ჯგუფის აქტიური წევრია, რომელიც შედგება ბიზნეს ლიდერებისგან მთელი მსოფლიოდან. 2013 წელს, მან უმასპინძლა ჩვენს, 
        კურსდამთავრებულთა ყოველწლიურ შეკრებას საქართველოში. ეს შეკრება იყო ყველაზე წარმატებული და გასაოცარი სიახლე ჩვენთვის. ჰარვარდელებმა 
        აღმოვაჩინეთ ულამაზესი საქართველო, მისი შეუფასებელი კულტურითა და სტუმართმოყვარე ხალხით. მამუკა ყოველთვის ხელს უწყობდა ქვეყნის 
        განვითარებას და ცნობადობის გაზრდას. იგი დაუღალავად შრომობდა იმისათვის, რომ საქართველოში არსებული სხვადასხვა ბიზნეს შესაძლებლობები 
        გაეცნო მსოფლიოს წამყვანი ბიზნესორგანიზაციებისთვის და მათი ხელმძღვანელებისთვის.
        მამუკამ მთელი მისი ცხოვრება საქართველოს აღმშენებლობას მიუძღვნა. მისმა აშკარა ძალისხმევამ და წარმატებამ, გააუმჯობესა 
        მრავალი ინდუსტრია, მათ შორის საბანკო სისტემა და მთელი ქვეყნის ეკონომიკა.
        ვიმედოვნებთ, რომ საქართველოს სასამართლო ამ ყველაფერს გაითვალისწინებს და გამოიტანს გამამართლებელ განაჩენს"-ნათქვამია მიმართვაში.

        მამუკა ხაზარაძისა და ბადრი ჯაფარიძის წინააღმდეგ გამოძიება პროკურატურამ 2018 წლის აგვისტოში დაიწყო, 2019 წლის ივლისში კი ბრალი წარუდგინა.
        მათ 17 მილიონ დოლარამდე უკანონო შემოსავლის ლეგალიზებას (ფულის გათეთრებას) ედავებიან.
        ავთანდილ წერეთელს კი, პროკურატურა ბიზნესმენს ბადრი ჯაფარიძისთვის და მამუკა ხაზარაძისთვის უკანონო შემოსავლების ლეგალიზებაში დახმარებას ედავება.
        საქალაქო სასამართლომ აღნიშნულ საქმეზე განაჩენი 11 იანვარს უნდა გამოაცხადოს.

    """

    answer = ["მამუკა ხაზარაძე", "ბადრი ჯაფარიძე", "ავთანდილ წერეთელი"]

    assert sorted(answer) == extract_persons(text)


def test_5():
    text = """  
       ახლა გადავდივართ კიდევ ახალ ეტაპზე – ეს გახლავთ „საქართველოს თავდაცვისა და შეკავების გაძლიერების ინიციატივა“, 
       რომელიც ხელს შეუწყობს საქართველოს თავდაცვის სამინისტროსა და თავდაცვის ძალების სტრუქტურის მოდერნიზაციას, რათა ის 
       თანხვედრაში იყოს ნატო-ს წევრი ქვეყნების თავდაცვის ძალების სტრუქტურებთან. ეს საკმაოდ მასშტაბური პროექტია და მჯერა, რომ საქართველოს თავდაცვის 
       ძალები და სამინისტრო ერთიანი ძალებით შეძლებენ ძალიან შთამბეჭდავი შედეგის მიღწევას“, – განაცხადა კელი დეგნანმა.

    """

    answer = ["კელი დეგნანი"]

    assert sorted(answer) == extract_persons(text)


def test_6():
    text = """  
       შესაძლოა "მთავარი არხის" დირექტორის პოსტი, ნიკა გვარამიამ დატოვოს. 
       მის შემცვლელად კი "ნაციონალური მოძრაობის" ყოფილი თავდაცვის მინისტრი, 
       დიმიტრი შაშკინი სახელდება. ინფორმაციას ამის შესახებ, "პრაიმტაიმი" ავრცელებს. 
    """
    answer = ["დიმიტრი შაშკინი", "ნიკა გვარამია"]

    assert sorted(answer) == extract_persons(text)


def test_7():
    text = """  
       შესაძლოა "მთავარი არხის" დირექტორის პოსტი, ნიკა გვარამიამ დატოვოს. 
       მის შემცვლელად კი "ნაციონალური მოძრაობის" ყოფილი თავდაცვის მინისტრი, 
       დიმიტრი შაშკინი სახელდება. ინფორმაციას ამის შესახებ, "პრაიმტაიმი" ავრცელებს. 
    """
    answer = ["დიმიტრი შაშკინი", "ნიკა გვარამია"]

    assert sorted(answer) == extract_persons(text)


def test_8():
    text = """  
       „ბიზნესპარტნიორის“ ექსკლუზიური ინტერვიუ კელი დეგნანთან - ქართველებს საოცარი გამონათქვამი გაქვთ, „ძალა ერთობაშია“, ნამდვილად ერთიანობაშია სიძლიერე.
       
    """
    answer = ["კელი დეგნანი"]

    assert sorted(answer) == extract_persons(text)


def test_9():
    text = """  
        გიორგი ამაშუკელზე რაღაც წერია აქ, ისევე როგორც მიხეილ ჩხენკელზე და ირაკლი ღარიბაშვილთან ვიღაც ადამიანის ვიზიტზე ბიძინა ივანიშვილისთვის რაღაცის გადასაცემად. 
    """
    answer = [
        "გიორგი ამაშუკელი",
        "მიხეილ ჩხენკელი",
        "ირაკლი ღარიბაშვილი",
        "ბიძინა ივანიშვილი",
    ]

    assert sorted(answer) == extract_persons(text)


def test_10():
    # test that we can idntify full parliamentars list from their site - meaning we do not miss important name and/or surname
    text = """გიორგი ამილახვარი, თეონა აქუბარდია, არმაზ ახვლედიანი, დავით ბაქრაძე, გია ბენაშვილი, ლევან ბეჟაშვილი, ირაკლი (დაჩი) ბერაია, რამინა ბერაძე, მაია ბითაძე, თინათინ ბოკუჩავა, ანზორ ბოლქვაძე, ელისო ბოლქვაძე, გიორგი ბოტკოველი, მაკა ბოჭორიშვილი, ანა ბუჩუკური, გიორგი გოდაბრელიძე, ელგუჯა გოცირიძე, რომან გოცირიძე, ბექა დავითულიანი, ალექსანდრე დალაქიშვილი, ზაურ დარგალი, ისკო დასენი, მიხეილ დაუშვილი, ხატია დეკანოიძე, ზაალ დუგლაძე, ქეთევან დუმბაძე, ალექსანდრე ელისაშვილი, ავთანდილ ენუქიძე, გოჩა ენუქიძე, ლევან ვარშალომიძე, გიორგი ვაშაძე, გრიგოლ ვაშაძე, გიორგი ვოლსკი, ირმა ზავრადაშვილი, ირაკლი ზარქუა, დავით ზილფიმიანი, არჩილ თალაკვაძე, ედიშერ თოლორაია, ფრიდონ ინჯია, ნინო იობაშვილი, რატი იონათამიშვილი, ლევან იოსელიანი, აბდულა ისმაილოვი, დავით კაჭარავა, ვლადიმერ კახაძე, გიორგი კახიანი, კახა კახიშვილი, შალვა კერესელიძე, პაატა კვიჟინაძე, მანუჩარ კვირკელია, ხათუნა კვიციანი, ვახტანგ კიკაბიძე, დავით კირკიტაძე, სუმბატ კიურეღიან, ირაკლი კობახიძე, ლევან კობიაშვილი, ირაკლი კოვზანაძე, რესან კონცელიძე, თამარ კორძაია, კახაბერ კუჭავა, მარიამ ლაშხი, ბექა ლილუაშვილი, ზაზა ლომინაძე, დავითი მათიკაშვილი, ნონა მამულაშვილი, სამველ მანუკიან, პაატა მანჯგალაძე, გურამ მაჭარაშვილი, ნიკა მაჭუტაძე, ლევან მგალობლიშვილი, მამუკა მდინარაძე, ვახტანგი მეგრელიშვილი, ირაკლი მეზურნიშვილი, მაია მენაღარიშვილი, გოგი მეშველიანი, ირაკლი მეძმარიაშვილი, აკაკი მინაშვილი, სავალან მირზოევი, გივი მიქანაძე, გელა მიქაძე, ზაალ მიქელაძე, ალექსანდრე მოწერელია, შალვა ნათელაშვილი, ტარიელ ნაკაიძე, კობა ნაყოფია, ანა ნაცვლიშვილი, რამაზ ნიკოლაიშვილი, ანტონ ობოლაშვილი, ბექა ოდიშარია, კახაბერ ოქრიაშვილი, ანრი ოხანაშვილი, შალვა პაპუაშვილი, ალექსანდრე რაქვიაშვილი, ჰერმან საბო, სალომე სამადაშვილი, ხათუნა სამნიძე, გელა სამხარაული, დიმიტრი სამხარაძე, ნიკოლოზ სამხარაძე, გუბაზ სანიკიძე, ვიქტორ სანიკიძე, მიხეილ სარჯველაძე, დავით სერგეენკო, ეკა სეფაშვილი, სულხან სიბაშვილი, დავით სონღულაშვილი, სოზარ სუბარი, ალექსანდრე ტაბატაძე, თამარ ტალიაშვილი, ნოდარ ტურძელაძე, ზაალ უდუმაშვილი, დავით უსუფაშვილი, ირაკლი ქადაგიშვილი, ბაჩუკი ქარდავა, ლევან ქარუმიძე, ალუდა ღუდუშაური, მიხეილ ყაველაშვილი, შალვა შავგულიძე, გოდერძი ჩანქსელიანი, თამარ ჩარკვიანი, ვლადიმერ ჩაჩიბაია, ვასილ ჩიგოგიძე, ირაკლი ჩიქოვანი, ცეზარი ჩოჩელი, ნატო ჩხეიძე, როსტომ ჩხეიძე, ბეჟან წაქაძე, ანა წითლიძე, ნინო წილოსანი, ხატია წილოსანი, დევი ჭანკოტაძე, გივი ჭიჭინაძე, შოთა ხაბარელი, ლევან ხაბეიშვილი, დილარ ხაბულიანი, ირაკლი ხახუბია, დავით ხაჯიშვილი, გიორგი ხელაშვილი, ეკატერინე ხერხეულიძე, იაგო ხვიჩია, ელენე ხოშტარია, გიორგი ხოჯევანიშვილი, დიმიტრი ხუნდაძე, თეიმურაზ ჯანაშია, ბადრი ჯაფარიძე, ვიქტორ ჯაფარიძე, """

    answer = [
        "გიორგი ამილახვარი",
        "თეონა აქუბარდია",
        "არმაზ ახვლედიანი",
        "დავით ბაქრაძე",
        "გია ბენაშვილი",
        "ლევან ბეჟაშვილი",
        "ირაკლი დაჩი ბერაია",
        "რამინა ბერაძე",
        "მაია ბითაძე",
        "თინათინ ბოკუჩავა",
        "ანზორ ბოლქვაძე",
        "ელისო ბოლქვაძე",
        "გიორგი ბოტკოველი",
        "მაკა ბოჭორიშვილი",
        "ანა ბუჩუკური",
        "გიორგი გოდაბრელიძე",
        "ელგუჯა გოცირიძე",
        "რომან გოცირიძე",
        "ბექა დავითულიანი",
        "ალექსანდრე დალაქიშვილი",
        "ზაურ დარგალი",
        "ისკო დასენი",
        "მიხეილ დაუშვილი",
        "ხატია დეკანოიძე",
        "ზაალ დუგლაძე",
        "ქეთევან დუმბაძე",
        "ალექსანდრე ელისაშვილი",
        "ავთანდილ ენუქიძე",
        "გოჩა ენუქიძე",
        "ლევან ვარშალომიძე",
        "გიორგი ვაშაძე",
        "გრიგოლ ვაშაძე",
        "გიორგი ვოლსკი",
        "ირმა ზავრადაშვილი",
        "ირაკლი ზარქუა",
        "დავით ზილფიმიანი",
        "არჩილ თალაკვაძე",
        "ედიშერ თოლორაია",
        "ფრიდონ ინჯია",
        "ნინო იობაშვილი",
        "რატი იონათამიშვილი",
        "ლევან იოსელიანი",
        "აბდულა ისმაილოვი",
        "დავით კაჭარავა",
        "ვლადიმერ კახაძე",
        "გიორგი კახიანი",
        "კახა კახიშვილი",
        "შალვა კერესელიძე",
        "პაატა კვიჟინაძე",
        "მანუჩარ კვირკელია",
        "ხათუნა კვიციანი",
        "ვახტანგ კიკაბიძე",
        "დავით კირკიტაძე",
        "სუმბატ კიურეღიან",
        "ირაკლი კობახიძე",
        "ლევან კობიაშვილი",
        "ირაკლი კოვზანაძე",
        "რესან კონცელიძე",
        "თამარ კორძაია",
        "კახაბერ კუჭავა",
        "მარიამ ლაშხი",
        "ბექა ლილუაშვილი",
        "ზაზა ლომინაძე",
        "დავითი მათიკაშვილი",
        "ნონა მამულაშვილი",
        "სამველ მანუკიან",
        "პაატა მანჯგალაძე",
        "გურამ მაჭარაშვილი",
        "ნიკა მაჭუტაძე",
        "ლევან მგალობლიშვილი",
        "მამუკა მდინარაძე",
        "ვახტანგი მეგრელიშვილი",
        "ირაკლი მეზურნიშვილი",
        "მაია მენაღარიშვილი",
        "გოგი მეშველიანი",
        "ირაკლი მეძმარიაშვილი",
        "აკაკი მინაშვილი",
        "სავალან მირზოევი",
        "გივი მიქანაძე",
        "გელა მიქაძე",
        "ზაალ მიქელაძე",
        "ალექსანდრე მოწერელია",
        "შალვა ნათელაშვილი",
        "ტარიელ ნაკაიძე",
        "კობა ნაყოფია",
        "ანა ნაცვლიშვილი",
        "რამაზ ნიკოლაიშვილი",
        "ანტონ ობოლაშვილი",
        "ბექა ოდიშარია",
        "კახაბერ ოქრიაშვილი",
        "ანრი ოხანაშვილი",
        "შალვა პაპუაშვილი",
        "ალექსანდრე რაქვიაშვილი",
        "ჰერმან საბო",
        "სალომე სამადაშვილი",
        "ხათუნა სამნიძე",
        "გელა სამხარაული",
        "დიმიტრი სამხარაძე",
        "ნიკოლოზ სამხარაძე",
        "გუბაზ სანიკიძე",
        "ვიქტორ სანიკიძე",
        "მიხეილ სარჯველაძე",
        "დავით სერგეენკო",
        "ეკა სეფაშვილი",
        "სულხან სიბაშვილი",
        "დავით სონღულაშვილი",
        "სოზარ სუბარი",
        "ალექსანდრე ტაბატაძე",
        "თამარ ტალიაშვილი",
        "ნოდარ ტურძელაძე",
        "ზაალ უდუმაშვილი",
        "დავით უსუფაშვილი",
        "ირაკლი ქადაგიშვილი",
        "ბაჩუკი ქარდავა",
        "ლევან ქარუმიძე",
        "ალუდა ღუდუშაური",
        "მიხეილ ყაველაშვილი",
        "შალვა შავგულიძე",
        "გოდერძი ჩანქსელიანი",
        "თამარ ჩარკვიანი",
        "ვლადიმერ ჩაჩიბაია",
        "ვასილ ჩიგოგიძე",
        "ირაკლი ჩიქოვანი",
        "ცეზარი ჩოჩელი",
        "ნატო ჩხეიძე",
        "როსტომ ჩხეიძე",
        "ბეჟან წაქაძე",
        "ანა წითლიძე",
        "ნინო წილოსანი",
        "ხატია წილოსანი",
        "დევი ჭანკოტაძე",
        "გივი ჭიჭინაძე",
        "შოთა ხაბარელი",
        "ლევან ხაბეიშვილი",
        "დილარ ხაბულიანი",
        "ირაკლი ხახუბია",
        "დავით ხაჯიშვილი",
        "გიორგი ხელაშვილი",
        "ეკატერინე ხერხეულიძე",
        "იაგო ხვიჩია",
        "ელენე ხოშტარია",
        "გიორგი ხოჯევანიშვილი",
        "დიმიტრი ხუნდაძე",
        "თეიმურაზ ჯანაშია",
        "ბადრი ჯაფარიძე",
        "ვიქტორ ჯაფარიძე",
    ]

    assert sorted(answer) == extract_persons(text)


def test_11():
    text = """ჩრდილოეთ კორეის ლიდერმა, კიმ ჩენ ინმა მოსახლეობას მოუწოდა, რთული პერიოდისთვის მოემზადონ - ქვეყანას საკვების დეფიციტი და ეკონომიკური არასტაბილურობა ემუქრება, ამის შესახებ BBC წერს. ​"""

    answer = ["კიმ ჩენ ინი"]

    assert sorted(answer) == extract_persons(text)


def test_12():
    text = """ზურაბ გირჩი ჯაფარიძე - საჯაროდ ვკითხულობ, იტყუება ენმ-ის ლიდერი? რა მოლაპარაკებების ჩაშლაზე ლაპარაკობს?"""

    answer = ["ზურაბ გირჩი ჯაფარიძე"]
    assert sorted(answer) == extract_persons(text)


def test_13():
    text = """გიგი უგულავა ზაალ უდუმაშვილს მიმართავს - ზუგდიდი ირჩევს ზუგდიდელსო, ძვირფასო მეგობარო, ხომ ვერ მეტყვი, სანდრა რულოვსი ზუგდიდის რომელი სოფლიდან ან უბნიდანაა, ზუგდიდში რომ იყრიდა კენჭს"""

    answer = ["გიგი უგულავა", "ზაალ უდუმაშვილი", "სანდრა რულოვსი"]
    assert sorted(answer) == extract_persons(text)


def test_14():
    text = """სანდრა ელისაბედ რულოვსმა სისხლი უანგაროდ გაიღო"""

    answer = ["სანდრა ელისაბედ რულოვსი"]
    assert sorted(answer) == extract_persons(text)


def test_14_1():
    text = """სანდრა-ელისაბედ რულოვსმა სისხლი უანგაროდ გაიღო"""

    answer = ["სანდრა ელისაბედ რულოვსი"]
    assert sorted(answer) == extract_persons(text)


def test_15():
    text = "ელის-მარია სააკაშვილმა"
    answer = ["ელის მარია სააკაშვილი"]

    assert sorted(answer) == extract_persons(text)


def test_15_1():
    text = "ელის მარია სააკაშვილმა"
    answer = ["ელის მარია სააკაშვილი"]

    assert sorted(answer) == extract_persons(text)


def test_16():
    text = "გიორგი (დავით) გვარამია იყო და არა იყო რა"
    answer = ["გიორგი დავით გვარამია"]

    assert sorted(answer) == extract_persons(text)
