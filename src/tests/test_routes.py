def test_bage_page_get(app, client):
    res = client.get('/')
    assert res.status_code == 200

def test_drivers_page_get(app, client):
    res = client.get('/drivers')
    assert res.status_code == 200

def test_report_page_get(app, client):
    res = client.get('/report')
    assert res.status_code == 200