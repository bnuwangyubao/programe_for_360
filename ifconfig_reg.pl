#!/usr/bin/perl

use strict;
use Sys::HostAddr;
use Data::Dumper;
my $sysaddr=Sys::HostAddr->new();
my $ip_addr=$sysaddr->ip();
foreach my $interface(keys%{$ip_addr})
{
	foreach my $aref(@{$ip_addr->{$interface}})

	{
		printf("$interface $aref->{address}\n")
	}	
}
