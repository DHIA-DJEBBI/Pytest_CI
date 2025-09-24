import pytest , time 


def run_simmultion_step():

    time.sleep(3)
    return True
def test_run_time_simulation(): 

    start = time.time()
    result = run_simmultion_step() 
    end = time.time()
    duration = end - start 
    assert result == True 
    assert duration > 3 , f"simulation trop lente ({duration:.3f}s)"


    


