# Django Book Shelf Project
This is  a django project that shelfs books

This shelf can allow admin users perform the following operationns
 * Adding new books
 * Archiving stolen or lost books
 * Delete books

This project was done using [Python Programming Language](https://www.python.org) and the [Django Web FrameWork](https://www.djangoproject.com)

----------------------------------

## Here are the steps in Running the project.
1. Start your code editor preferably visual studio code
2. Open the folder that contains the bookshelf project after ypu have cloned it
3. Intalll the crispy forms library
4. Next run `python manage.py migrate` to migrate all models to the database schema
5. Next run  `python manage.py makemigrations`, this will automatically make migrations for all the app present in the project folder
6. Next run `python manage.py migrate` again to finally move all migrations
7. Finally you can run the python server using `python manage.py runserver` you can decide to add your desired port number e.g `python manage.py runserver 5000`. This is how we run teh server if we wanted to use port 50000
8. Our server should be up and running
-----------------------
### Creating our SuperUser
1. Quit the server by using the keyboard interrupt `CTRL + C`
2. Run the create superuser command using `python manage.py createsuperuser`
3. This will prompt us for our details such as username, email address, password and password agai which is to validate our password
  * `Enter Username(hit enter to use the default omputer name)`
  * `Email Address` hit enter to leave blank
  *  `Enter password` and 
  *  `Enter password (again)` 
  *  With this few steps our superuser has been created
4. Re-run the server again
----------------------------------------
## Operating the Book Shelf Project
> After we run our Python server running on `port 8000`
> The default page takes us to the index page which is the `book_list.html` page 


* The booklist page is like this 
Endpoint `http://127.0.0.1/` - Represents the book list view
![homepage-no-book](https://user-images.githubusercontent.com/55829039/166106798-4dbdaa14-b6d1-4053-976f-58fd22ba54f0.png)

* Next we login our superuser
Endpoint `http://127.0.0.1:8000/users/login` - Representing the users login page
 ![login-admin](https://user-images.githubusercontent.com/55829039/166106859-2896fed8-622b-4100-aad9-673123efdefc.png)


* After logging in as super user we'll be redirected to the homepage which contains no book, let us add new books,
Endpoint `http://127.0.0.1:8000/users/login`
Use *username=admin* and *password=admin*
![admin-no-book](https://user-images.githubusercontent.com/55829039/166106875-43c128fc-50b6-4e99-b29e-9d2af2115f52.png)


* Our add a new book page looks like this
Endpoint `http://127.0.0.1:8000/new` back to the list but now we have been authenticated as a superuser
![amin-add-new](https://user-images.githubusercontent.com/55829039/166106884-4704960c-0bfa-4c6f-a411-6d205efde00d.png)


After adding some images we'll have these view
Endpoint `http://127.0.0.1:8000/`- for the first page showing only three books
![admin-added-image1](https://user-images.githubusercontent.com/55829039/166106936-5d076f5a-5f1a-4c71-aebf-41433db7d185.png)

Endpoint `http://127.0.0.1:8000/?page=2` - For the second page 
![admin-added-image2](https://user-images.githubusercontent.com/55829039/166106962-572b3f93-9673-46d2-8458-624b194722fa.png)

Endpoint `http://127.0.0.1:8000/?page=3`
![admin-added-image3](https://user-images.githubusercontent.com/55829039/166106982-b4e339e4-0115-4a7b-a23b-ccbf47ab5206.png)

**Note:** It can contain as many endpoints we want as long as we continue to add images

* Checking the details of what we have built looks like this 
Endpoint `http://127.0.0.1:8000/book/detail/9` - Gives the detail of the 9th book
![admin-detail-page-1](https://user-images.githubusercontent.com/55829039/166107016-f6b52bc8-1010-4d3d-ae53-62baba8b562f.png)
![admin-detail-page-2](https://user-images.githubusercontent.com/55829039/166107021-08f3c8fd-6124-4d15-8a28-f9ff6f8b6d4a.png)

* Editing the the books have the following look 
Endpoint `http://127.0.0.1:8000/book/edit/9` - This is the endpoint for editing item 9
![admin-edit-page-1](https://user-images.githubusercontent.com/55829039/166107072-a6791725-ad3f-4e77-9edf-ada3a153988c.png)
![admin-edit-page-2](https://user-images.githubusercontent.com/55829039/166107040-a839cee0-c43c-48f7-96f3-abb0d5613c5a.png)

* Archiving the book looks like
Endpoint `http://127.0.0.1:8000/book/archive/9` for archiving the 9th object
![admin-archived-images](https://user-images.githubusercontent.com/55829039/166107087-f7f7260e-251e-49c7-9462-1cba1b194e0c.png)

* Deleting a book looks like 
Endpoint `http://127.0.0.1:8000/book/delete/3` for deleting teh 3rd Item
![admin-confirm-delete-page](https://user-images.githubusercontent.com/55829039/166107102-aeae42c7-e2c1-42b7-a3f2-232db09efab5.png)

* Logging Out looks like 
Endpoint `http://127.0.0.1:8000/users/logout` to log the user out
![login-admin](https://user-images.githubusercontent.com/55829039/166107173-197093f7-6623-46c6-9613-4bbe14d84000.png)

* Registering another user whi is not a superuser and viewing the details of each book. Meanwhile for every other view operations is not functional because he/she is not admin

* Active user sign up i.e means a user that is not a superuser
![new-user-signin](https://user-images.githubusercontent.com/55829039/166107188-4aa1f379-e42a-4aa4-9eba-7ec16ec58a24.png)
![active-user-login](https://user-images.githubusercontent.com/55829039/166107205-0f1197be-412d-49f6-962b-f05901d7dc36.png)
![incorrect-login-details](https://user-images.githubusercontent.com/55829039/166107233-6d65bac0-f369-49f0-a6d1-2bc866c053ad.png)
![active-user-login-homepage](https://user-images.githubusercontent.com/55829039/166107260-fa5e4173-5852-495b-bdd7-164cb73b94d6.png)
![active-user-detail-page-1](https://user-images.githubusercontent.com/55829039/166107271-6f973e91-9060-4492-9d0e-d6632375f3b3.png)
![active-user-detail-page-2](https://user-images.githubusercontent.com/55829039/166107289-cb7cc2e6-c345-4dbb-880b-63953ab890c5.png)

