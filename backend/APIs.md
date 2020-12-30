# api

| 기능                        | url                                 | method   | req  | res  |
| --------------------------- | ----------------------------------- | -------- | ---- | ---- |
| **게시글 관련**             | api/v1/articles/                    |          |      |      |
| 게시글 전체 조회            | /                                   | GET      |      |      |
| 게시글 작성                 | /                                   | POST     |      |      |
| 게시글 수정                 | `<int:article_pk>`/                 | PUT      |      |      |
| 게시글 삭제                 | `<int:article_pk>`/                 | DELETE   |      |      |
| 게시글 디테일 조회          | `<int:article_pk>/`                 | GET      |      |      |
| 게시글 댓글 조회            | `<int:article_pk>/comments/`        | GET      |      |      |
| 게시글 댓글 작성            | `<int:article_pk>/comments/`        | POST     |      |      |
| 게시글 댓글 삭제            | `<int:comment_pk>`/comments_delete/ | DELETE   |      |      |
| 회원 작성글 조회            | `<int:user_id>`/profile_articles/   | GET      |      |      |
| 회원 작성댓글 조회          | `<int:user_id>`/profile_comments/   | GET      |      |      |
| 게시글 조회시 조회수 늘리기 | `<int:article_pk>`/read/            | POST     |      |      |
|                             |                                     |          |      |      |
|                             |                                     |          |      |      |
| **유저 관련**               | api/v1/accounts/                    |          |      |      |
| 회원가입                    | signup/                             | POST     |      |      |
| 로그인                      | api-token-auth/                     | POST     |      |      |
| 유저아디로 유저이름 얻기    | `<int:user_id>`/                    | GET      |      |      |
| 유저 좋아하는 영화 보냄     | `<int:user_id>`/recommend/          | GET      |      |      |
| 회원 포인트 조회            | `<int:user_id>/points/`             | GET      |      |      |
|                             |                                     |          |      |      |
|                             |                                     |          |      |      |
| **영화 관련**               | movies/                             |          |      |      |
| 영화데타들 요청             | /                                   | GET      |      |      |
| 영화데타 베스트5 요청       | bestFive/                           | GET      |      |      |
| 영화 상세정보 조회          | `<int:movie_id>`/                   | GET      |      |      |
| 영화 한줄평들 조회,생성     | `<int:movie_id>`/reviews/           | GET,POST |      |      |
| 영화 한줄평 삭제            | `<int:review_pk>/review_delete/`    | DELETE   |      |      |
| 추천 영화 저장              | forUserMovieSave/                   | POST     |      |      |
|                             |                                     |          |      |      |



