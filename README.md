# AirBnB_clone :house_with_garden:

![HBNB]("https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210218%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210218T155015Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=06aaa2dd7c094bbca45565ff5cb047d73dbc9f1e124d69be68b5b4710d22e019")

### Introduction:
This is the first step towards building our first full web application: the AirBnb clone. We must begin by writing a command interpreter to manage all the objects for AirBnb! We must also build a storage engine, with which the interpreter will interact. 
## Installation :hammer_and_wrench:
Clone AirBnB_clone repository:
```bash
git clone https://github.com/aleiadevore/AirBnB_clone.git
```

There are **two** ways in which the interpreter can be run:   
  _Interactive_ and _Non-Interactive modes._:  



### Interactive Mode:
> ```bash
> ./console.py
> (hbnb) <command>
> ```
### Non-Interactive Mode:
> ```bash
> echo "<command>" | ./console.py
>```
## Usage :woman_technologist:
The console accepts the following _commands_:  
  
> **create**  
**show**  
**destroy**  
**all**  
**update**

 
|Command|Description|Ex:|     
|----|-----|-------|     
|**create**|creates a new instance then prints it's _id_.|**create City**|
|**show**|shows instance based on _class name_ and _id_. |**show User 4555-4655-54585**|
|**destroy**|destroys an instance based on _class name_ and _id_. |**destroy Amenity**|
|**all**|prints all instances based or not on the _class name_|**all City**|
|| |**all**|
|**update**|Updates an instance based on the _class name_ and _id_ by adding or updating attribute|**update User 4654-4646-4654 name "Lemon"**|



## Contributing :fist_right::fist_left:
This project has been assigned under the curriculum offered by Holberton School. The contributors of this repository are:  
**Aleia Devore**  
**Bre Rickner**

## Issues :monocle_face:
This project is currently in progress and some issues are to be expected while construction is still underway :nerd_face: