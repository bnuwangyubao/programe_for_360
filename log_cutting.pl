#!/usr/bin/perl
use strict;
use warnings;
my $log="access.log";
while(1){
	my($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime;
	$year+=1900;
	$mon+=1;
	my $nlog=sprintf("access_%ddd.log",$year,$mon,$mday);
	rename $log,$nlog;
	`nginx -s reopen`;
	sleep(3600*24);
}
