# NowWeSeeYou
A django based portal integrated with OpenCV to automate attendance.

### Team - TheCodingCompany
Members - Lokesh Nirania (170010009),
          Deepak HR (170010026),
          Anudeep Tubati (170010039) and
          Rohan Shrothrium (170020031)

### The Problem Statement
Though attendance is an inevitable part of college, it is commonly taken for granted. There's always a trade-off in between the professor (for that matter, any human) wasting time on it or a lot of students getting proxies. It is a serious issue and also we were thinking of a solution in the lines of Image processing and ML (something which everyone at least hears these days, if not interested in).

### The Idea
- The first idea that comes to anyones mind when they hear about automating attendance would be keeping a camera such that all the students can be seen. But the problems associated with this idea were that we'd need a high resolution camera (enough to distinguish in between the back benchers) and also we would have to keep track of people who are sleeping, going out or doing some other activity which makes their face less (or not at all) visible.
- So the next sensible thing we could think of was to keep 2 cameras at the entrance, facing in the opposite directions so that incoming and outgoing students can be distinguished.

### Putting it in practice
#### 1) Face Recognition
- For face recognition, we found some really good OpenCV articles to take our code base from [PyImageSearch](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/) and [ElectronicsForU](https://electronicsforu.com/electronics-projects/real-time-face-recognition-python-opencv).
- We soon found that the former one was better in practice, as
  - 128-D embeddings are used for storing facial data, making it train much faster and use less memory
  - The standard HaaR cascade classifier is coupled with an SVM
- Using better quality images, changing some dimensions of the frames and using slightly different decision boundary produced a good model.

#### 2) WebApp
- The webapp was made using django majorly. Here you could find all the details of courses, attendance and any other relevant material you've registered to.
- The main features of this webapp are
  - Notification if you missed a class, to eliminate any errors caused by the automation
  - Encourage the students whose attendance is below the required level
  
### To-Do
  - [ ] Bind facial data with body data (shirt colour, pant colour etc.) to prevent students from going out of the class by hiding their face
  - [ ] Use Celery library to automate the process of sending emails and starting attendance for a class
  - [ ] Store photos of every face recorded to correct mismatches better
  - [ ] Sending weekly reports to Professors
