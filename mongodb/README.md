# MongoDB Interview Questions

## 1. What is MongoDB?
MongoDB is a NoSQL database that provides high performance, high availability, and easy scalability.


## 2. What is NoSQL?
NoSQL stands for "Not Only SQL." It is a type of database that provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases.


## 3. Explain the BSON data format.
BSON (Binary JSON) is a binary-encoded serialization of JSON-like documents. It extends the JSON model to provide additional data types and to be efficient for encoding and decoding within different languages.


## 4. What is a Document in MongoDB?
A document is a basic unit of data in MongoDB, similar to a record in a relational database. It is a JSON-like representation of data, consisting of key-value pairs.

## 5. Explain the structure of a MongoDB document.
A MongoDB document consists of a set of key-value pairs. Keys are strings, and values can be various data types, including other documents, arrays, and arrays of documents.


## 6. What is a Collection in MongoDB?
A collection is a group of MongoDB documents. It is the equivalent of a table in a relational database.


## 7. What is the difference between MongoDB and RDBMS?
MongoDB is a NoSQL, document-oriented database, while RDBMS (Relational Database Management System) is a traditional relational database. MongoDB is schema-less and uses a flexible, JSON-like document model.


## 8. Explain indexing in MongoDB.
Indexes in MongoDB improve the performance of queries by allowing the database to locate data more quickly. MongoDB uses B-tree indexes.


## 9. What is sharding in MongoDB?
Sharding is the process of storing data records across multiple machines to improve scalability. It is MongoDB's approach to meeting the demands of data growth.


## 10. How does MongoDB ensure high availability?
MongoDB ensures high availability through features like replication. In a replica set, data is replicated to multiple nodes, providing redundancy and fault tolerance.


## 11. Explain the Aggregation Framework in MongoDB.
The Aggregation Framework is a powerful feature in MongoDB for data transformation and analysis. It allows you to process data documents and return computed results.


## 12. What is GridFS in MongoDB?
GridFS is a specification for storing and retrieving large files such as images, videos, and audio files in MongoDB.
