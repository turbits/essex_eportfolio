# University of Essex - ePortfolio

Author: Trevor Woodman

Site: https://essex.trevorwoodman.ca

This eportfolio is a repository of code, reflective pieces, and other essays as required by several _University of Essex, Post Graduate Computer Science Degree_ courses.

I have set up a basic Jekyll site to display this ePortfolio. The site is hosted using GitHub pages.

## Build Project

- Install Ruby w/ DevKit ~>3.1.3, run ridk install and select MSYS2 and MINGW development toolchain from the options (3)
- Open a new terminal window (PATH changes)
- Install bundler: `gem install bundler`
- Navigate to the root of the project
- Run `bundle install`
- Run `bundle exec jekyll serve`

## Deployment

Needs to be set up to use GitHub workflow but don't have time.

- Run project to build `bundle exec jekyll serve`
- In terminal, navigate to `_site` folder
- Run `scp -r . <username>@<ip>:/var/www/essex.trevorwoodman.ca/html/`

## Miscellaneous

A copy of the Gemfile because I don't trust like that:

```ruby
source "https://rubygems.org"

gem "jekyll", "~> 4.3.1"
gemspec
```

## Disclaimer Block For Code

> ⚠️ DISCLAIMER ⚠️
> 
> This project is a prototype for a University project, and should not be viewed as a production-ready app. You should not expect that it is secure. It employs techniques that were taught during the course of the module in a clear and sometimes verbose manner to demonstrate concepts, learning process, and ability. Do not use any of the code presented here in a production environment.
