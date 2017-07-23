#!/usr/bin/perl
## Copyright 2014 tkorays. All rights reserved.
## author tkorays
## email tkorays@hotmail.com

use strict;
use warnings;
use LWP;
use LWP::Simple;
use LWP::UserAgent;
use HTTP::Cookies;
use HTTP::Headers;
use HTTP::Response;
use Encode;
use URI::Escape;
use URI::URL;

my $email = '18215696665';
my $password = 'lilong0221??';
my $domain = 'down.51cto.com';
my $hostid='';
my $requestToken='';
my $rtk='';
my $channel='renren';

my $ua = LWP::UserAgent->new;
$ua->agent("Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0");
my $cookie_jar = HTTP::Cookies->new(
    file=>'lwp_cookies.txt',
    autosave=>1,
    ignore_discard=>1);
$ua->cookie_jar($cookie_jar);

my $login_url = 'http://home.51cto.com/index/?reback=http%3A%2F%2Fdown.51cto.com';

# 这里面没有判断是否需要验证码，聪明的你学完后肯定知道怎么搞定的
# # 人人是post登陆的，第一个参数是登陆的地址，第二个参数是一个匿名hash

my $res = $ua->post($login_url,{
        'email'=>$email,
        'password'=>$password,
        'domain'=>$domain});
my $homepage; 

#判断响应头里面的location，确定是否登陆成功   
if($res->header('Location') eq 'http://down.51cto.com/'){
    print 'login ok...',"\n";
    $homepage = $ua->get('http://down.51cto.com/'); 
}else{
    exit;
}
