# University of Essex - ePortfolio

Author: Trevor Woodman

Site: https://essex.trevorwoodman.ca

This ePortfolio is a repository of code, reflective pieces, and other essays as required by several _University of Essex, Post Graduate Computer Science Degree_ courses.

I have set up a basic Jekyll site to display this ePortfolio. I self-host this site instead of using GitHub pages. If you are marking a particular module and are concerned of the state of the site at the time of marking; I do not modify the content of the site from the time I submit it to the module until the beginning of another one. You can verify this is true by checking when `main` was last updated.

I solemnly swear to not update the live site post submission and before the start of another module with the exception being a correction relating to mine or others' privacy, or a significant error in the content unrelated to the coursework I have submitted. Any critical changes will be clearly documented on commit.

## Build Project

- Install [Ruby w/ DevKit ~>3.1.3 (>=3 but <4)](https://rubyinstaller.org/downloads/), run ridk install and select MSYS2 and MINGW development toolchain from the options (3)
- Open a new terminal window (PATH changes)
- Install bundler: `gem install bundler`
- Navigate to the root of the project
- Run `bundle install`
- Run `bundle exec jekyll serve`

## Deployment (notes for me)

Needs to be set up to use GitHub workflow but don't have time.

- Run project to build `bundle exec jekyll serve`
- In terminal, navigate to `_site` folder
- Run `scp -r . <username>@<ip>:<dir>`

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
