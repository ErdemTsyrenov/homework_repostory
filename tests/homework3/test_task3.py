from homework3.task3 import make_filter


def test_default():
    sample_data = [
         {
             "name": "Bill",
             "last_name": "Gilbert",
             "occupation": "was here",
             "type": "person",
         },
         {
             "is_dead": True,
             "kind": "parrot",
             "type": "bird",
             "name": "polly"
         }
    ]
    assert make_filter(name='polly', type='bird').apply(sample_data) == \
           [sample_data[1]]
    assert \
        make_filter(last_name='Gilbert', type='person').apply(sample_data) == \
        [sample_data[0]]
    assert \
        make_filter(last_name='Gilbert', type='bird').apply(sample_data) == \
        []
    assert \
        make_filter(type='bird', occupation='was here').apply(sample_data) == \
        []
    assert make_filter(title='bird', home='was here').apply(sample_data) == \
           []
