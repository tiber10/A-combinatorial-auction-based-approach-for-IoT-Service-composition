# A-combinatorial-auction-based-approach-for-IoT-Service-composition
This project transforms the service composition problem into an optimization problem. Moreover, in this project we propose a combinatorial auction approach (the Or bids method) in order to provide the best services selection to construct the service composition.
The project in under review. Once its published, this repo will be updated

## Results and Discussion
This project was a shared project between Hana NECIB for her master's graduation and Me.
The input are the quality of services and randomly we generate the indicators. The Qos values are defined in a specific range . After that the data should be normalized for efficiency results. Service composition (output) is coded in a 1-dimensional array of two columns, represented in the Maximum of reputation and The minimum of other factors ( response time , distance , energy of the services and indicators ) and a set of indicators. The table below shows the quality of services and their range.

![screen1](https://user-images.githubusercontent.com/40090186/181361086-b7439c63-f46e-44e7-88b8-7799a374a336.PNG)

The process of the system, was carried in Pycharm platform. The process went for 100 generation with a population size of 80. the figures below shows the Pareto fronts of the first generation and the fronts of the last generation.

![cap2](https://user-images.githubusercontent.com/40090186/181361489-195f0da2-9778-4686-b3ed-b675d015c71d.PNG)

![cap3](https://user-images.githubusercontent.com/40090186/181361505-321ea582-3808-4861-b4ed-0d67d77d5c46.PNG)

At the end of this process and after selecting the best service composition in this generation, we shows up the indicators selected for supplying the farm with water in different ways. The blue colors are the open gates (1) while the yellow ones are the closed gates (0).

![dsdas](https://user-images.githubusercontent.com/40090186/181362092-10b9d7ee-f7b7-4107-88da-78c33dc6e119.PNG)
