# Moving and processing data

## A general definition

- Data processing: converting raw data into meaningful information.

## Data processing value

- Conceptually
  - Remove unwanted data;
  - Optimize memory, process and network costs;
  - Convert data from one type to another;
  - Organize data;
  - To fit into a schema/structure;
  - Increase productivity.

## How data engineers process data

- Data manipulation, cleaning, and tidying tasks;
  - that can be automated;
  - that will always need to be done;
- Store data in a sanely structured database;
- Create views on top of the database tables;
- Optimizing the performance of the database.

## Scheduling

- Can apply to any task listed in data processing;
- Scheduling is the glue of your system;
- Holds each piece and organize how they work together;
- Runs tasks in a specific order and resolvers all dependencies.

### Manual, time and sensor scheduling

- Manually. Example: manually update the emmployee table;
- Automatically run at a specific table. Example: update the employee table at 6 AM;
- Automatically run if a specific condition is met
  - Sensor scheduling. Example: update the department tables if a new employee was added.

### Batches and streams

Data can be ingested in batches or streaming.

- Batches 
  - Group records at intervals;
  - Often cheaper because you can schedule it.
- Streams
  - Send individual records right away.

## Benefits and risks of parallel computing

- Advantages
  - Extra processing power;
  - Reduced memory footprint;
- Disavantages
  - Moving data incurs a cost;
  - Communication time.

## Cloud computing for data processing

- Servers on premises:
  - Bought;
  - Need space;
  - Electrical and maintenance cost;
  - Enough power for peak moments;
  - Processing power unused at quieter times.

- Servers on the cloud
  - Rented;
  - Don't need space;
  - Use just the resources we need;
  - When we need them;
  - The closer to the user the better.

### Cloud computing for data storage

- Database reliability: data replication;
- Risk with sensitive data.

### Multicloud

- Pros
  - Reducing reliance on a single vendor;
  - Cost-efficiences;
  - Local laws requiring certain data to be phisically present within the country;
  - Mitigating against disasters.
- Cons
  - Cloud providers try to lock in consumers;
  - Incompatibility;
  - Reduce Security and governance concerns.
