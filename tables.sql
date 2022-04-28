CREATE TABLE tvshow (
   TVShowID varchar(10),
   Title varchar(50) ,
   Year integer,
   Director varchar(50),
   Released date,
   Actors varchar(100),
   Language varchar(10),
   imdbRating decimal(1)
);

insert into tvshow values('tt2806718','Games of Thrones',2012,'N/A','2012-04-23','ABC','English',4.3);
insert into tvshow values('tt2806719','Games of Thrones',2012,'N/A','2012-04-30','ABC1','English',9.3);
