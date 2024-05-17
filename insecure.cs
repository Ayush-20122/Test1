var blogs = context.Posts
    .FromRawSql("SELECT * FROM Posts WHERE state = {0} AND author = {1}", state, author)
    .ToList();
