import pytest
import fonctions as f

def test_1():

	assert f.puissance(2,3) == 8
	assert f.puissance(2,2) == 4

def test_2():
	assert f.puissance(-1,2) == 1
	assert f.puissance(-1,3) == -1
	assert f.puissance(-1,-1) == -1
	assert f.puissance(-1,-2) == 1
	assert f.puissance(1,2) == 1

#Vérifi eque x>0 on a bien 0^x=0

def operation(): 
	assert f.puissance(0,1)==0
	assert f.puissance(0,5)==0
	assert f.puissance(0,100)==0

def test_exc_1():
	with pytest.raises(<TYPE-EXCEPTION>):
		CODE-QUI-DOIT-LANCER-LEXCEPTION

def test_exc_1_raises():
	with pytest.raises(Exception):
		assert f.puissance(0,-1)
		assert f.puissance(0,-5)



