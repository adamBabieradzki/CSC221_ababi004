import city_country as cc

def test_city_country():
    try:
        assert cc.location("santiago","chile") == "santiago, chile"
    except AssertionError:
        print("Failed")
    except:
        print("Failed")
    else:
        print("Passed")
def test_city_country_population():
    try:
        assert cc.location("santiago", "chile",5000000) == "santiago, chile population - 5000000"
    except AssertionError:
        print("Failed")
    except:
        print("Failed")
    else:
        print("Passed")

test_city_country()
test_city_country_population()