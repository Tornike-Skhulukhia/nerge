"""
Some temporary scripts
"""
from pprint import pprint as pp
from person.get_quotes import get_quotes
from person.extract_en import get_persons_en
from person.get_quotes import _encode_quotes_in_quotes

# def test_():
#     text = """
#             უკრაინის პრეზიდენტმა ვლადიმერ ზელენსკიმ მიუნხენის უსაფრთხოების კონფერენციაზე
#              სიტყვით გამოსვლისას იმ ვითარებაზე ისაუბრა, რომელიც ქვეყნის შიგნით
#               მიმდინარეობს. როგორც ზელენსკი აღნიშნავს, უკრაინა ყველაფრისთვის მზად არის.

#             "კუბოებში ჩაწოლას და რუსი "სამხედროების" ლოდინს არ ვაპირებთ. ჩვენ
#             არავისზე თავდასხმას არ ვაპირებთ, თუმცა ყველაფრისთვის მზად ვართ."
#             - ამბობს უკრაინის პრეზიდენტი.
#         """
# "111, 222, 333 "444 555" 666 777" - აცხადებს მარიამ მარიამიძე
# „ნაციონალური მოძრაობის“ თავმჯდომარის, ნიკა მელიას განცხადებით, დღეს „ერთიანი ნაციონალური მოძრაობის“ პოლიტიკური საბჭოს სხდომა გაიმართა, რომელზეც გადაწყდა, რომ პარტიის ცენტრალური საკითხი არის მიხეილ სააკაშვილის სიცოცხლის გადარჩენა. ნიკა მელიას თქმით, სააკაშვილის ჯანმრთელობის მდგომარეობა დღითიდღე მძიმდება და აღნიშნა, რომ კონსილიუმის წევრები, უცხოელი ექიმები ერთხმად აღნიშნავენ, რომ მისი მკურნალობა საქართველოში შეუძლებელია. „მოგეხსენებათ, რომ სახალხო დამცველის მიერ შექმნილი კონსილიუმი, ცენტრი „ემპათია“, უცხოელი ექიმები, მიხეილ სააკაშვილის პირადი ექიმი ერთხმად აღნიშნავენ, რომ მიხეილ სააკაშვილის მძიმე ჯანმრთელობის მდგომარეობა, რომელიც დღითიდღე მძიმდება და მძიმდება, არ ექვემდებარება საქართველოში განკურნებას. აქედან გამომდინარე, ერთადერთი გზა მიხეილ სააკაშვილის სიცოცხლის გადარჩენის არის შემდეგი – მიხეილ სააკაშვილი იყოს გადაყვანილი ქვეყნის ფარგლებს გარეთ უცხოურ კლინიკაში, შესაბამისი მკურნალობის მისაღებად. ძალიან დასანანია, რომ ამ ჰუმანიტარული საკითხის გამო გვიწევს პოლიტიკური ბრძოლა. ჰუმანიტარულია ის საკითხი, რომელიც ადამიანის, ქვეყნის მესამე პრეზიდენტის, მიხეილ სააკაშვილის სიცოცხლეს ეხება“, – აღნიშნა მელიამ. მისივე თქმით, პარტიის ყველა აქტივობა დაუკავშირდება მიხეილ სააკაშვილის სიცოცხლის გადარჩენას. „ჩვენ ვიყავით ბრძოლაში და ვრჩებით ბრძოლაში იქამდე, ვიდრე არ იქნება უზრუნველყოფილი მისი სიცოცხლე და ჯანმრთელობა, რაც მიმაჩნია, არის თითოეული ჩვენი პარტიის წევრის, ამომრჩევლის, მხარდამჭერის მთავარი ცენტრალური საკითხი“, – განაცხადა ნიკა მელიამ. მისივე თქმით, 5 მარტიდან სხვადასხვა ქალაქში საპროტესტო აქციები გაიმართება. „სხვადასხვა ფორმისა და შინაარსის საპროტესტო აქტივობები გაიმართება სხვადასხვა ქალაქში. 5 მარტს, 17:00 საათზე რუსთაველის გამზირზე ველოდებით ქვეყნის მოსახლეობის იმ ნაწილს, რომელიც თვლის, რომ ეს ისტორიული უსამართლობა უნდა დასრულდეს და ამ ბრძოლაში არიან“, – განაცხადა ნიკა მელიამ.
text = """

By doing this, you will do 2 great things: You will not put Georgia on the list
             of wild countries and you will make Bidzina Ivanishvili very happy. He will have 2 prisoners at the same time,
              whom he cannot tolerate”, - wrote Paata Burchuladze’s.
              
              """


resp = get_persons_en(text)
print(resp)
