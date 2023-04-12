# What is data engineering?

## Data workflow

There are four general steps through which data flows within an organization:

1. Data collection and Storage: we collect and ingest data from web traffic, surveys, or media consumption for example. The Data is stored in raw format.
2. Data preparation: the next step is to prepare it, which includes "cleaning data", for instance, finding missing or duplicate values, and converting data into a more organized format.
3. Exploration and Visualization: Once the data is clean and organized, it can be exploited. We explore it, visualize it, build dashboards to track changes or compare two sets of data.
4. Experimentation and Prediction: Finally, once we have a good grasp of our data, we are ready to run experiments or buidl predictive models.

Data engineers are responsible for the first step of the process (sometimes for the second too). They have a great responsibility as they lay the ground work for data analysts, data scientists and machine learning engineers.

## Data Enginner

Data engineers deliver:
- the correct data;
- in the right form;
- to the right people;
- as efficiently as possible.

### A data engineer's responsibilities

- Ingest data from different sources (SQL and NoSQL);
- Optimize databases for analysis;
- Remove corrupted data;
- Develop, construct, test and maintain data architectures (such as databases and large-scale processing systems to process and handle massive amounts of data).

## Data engineers and big data

- Big data becomes the norm => data engineers are more and more needed;
- Big data:
  - Have to think about how to deal with its size;
  - So large: traditional methods don't work anymore.

## Big data growth

- Sensors and devices;
- Social media;
- Enterprise data;
- VoIP (voice communication, multimedia sessions).

### The five V's

Big data is commoly characterized by five Vs:

- Volume (how much?)
- Variety (what kind?)
- Velocity (how frequent?)
- Veracity (how accurate?)
- Value (how useful?)

## Data engineers vs data scientists

The data scientist is responsible for the data preparation, exploration and visualization, and experimentation and prediction;

- Data engineer
  - Ingest and store data;
  - Set up databases;
  - Build data pipelines;
  - Strong software skills.

- Data scientist
  - Exploit data;
  - Access databases;
  - Use pipelines outputs;
  - Strong analytical skills.
  
## The data pipeline

Data pipelines ensure an efficient flow of the data:

- Automate:
  - Extracting;
  - Transforming;
  - Combining;
  - Validating;
  - Loading.
- Reduce:
  - Human intervention;
  - Errors;
  - Time it takes data to flow.

### ETL and data pipelines

ETL:

- Popular framework for designing data pipelines
  1. **Extract** data;
  2. **Transform** extracted data;
  3. **Load** transformed data to another database.

Data pipelines:

- Move data from one system to another;
- May follow ETL;
- Data may not be transformed;
- Data may be directly loaded in application.
