"use strict";

module.exports = function(models) {
  var Account = models.Account;
  var Blog = models.Blog;
  return Account.create({
    username: "andy",
    password: "autida",
    firstname: "andy",
    lastname: "autida"
  }).then(function(account) {
    return Blog.create({
      title: "sample 1",
      body: "sample 1",
      created: new Date(),
      account_id: account.id
    });
  }).then(function(blog) {
    return Blog.create({
      title: "sample 2",
      body: "sample 2",
      created: new Date(),
      account_id: blog.account_id
    });
  });
}
