Cloud_Django:-

CLoud Django is a web app which serves as an Online cloud for file storage and for file sharing.  
It satisfies the following conditions:-  
	
	1)As a user, I should be able to login on the platform using email address and password.  

	2)As a logged-in user, I should be able to see a list of the all the files that I have uploaded. This list should be private and not visible to other users on the platform or to external parties.  
	
	3)As a logged-in user, I should be able to delete an already uploaded file.  

	4)As a logged-in user, I should be able to upload a new file while specifying some addition info such as a title, description, etc. Once uploaded, the platform should figure out the file type and optionally compress it for storage. The file size could be anything upto 1GB.  

	5)As a logged-in user, I should be able to share one of my files publicly using a tiny URL obtained from the system.  

For Setup Execute the following commands:-

git clone https://github.com/shyamsunder007/Cloud_Django.git
cd CLoud_Django
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Now check the localserver url('http://127.0.0.1:8000') in yur web browser