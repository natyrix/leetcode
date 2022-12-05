# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
delete p from Person pp, Person p where p.email=pp.email and pp.id<p.id