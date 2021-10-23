class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def isIPv4(IP):
            IP = IP.split('.')
            if len(IP) != 4: return False
            for ip in IP:
                if (len(ip) > 1 and ip[0] == '0') or ip=='': return False
                for a in ip:
                    if not '0'<=a<='9': return False
                if not 0<=int(ip)<=255: return False
            return True

        def isIPv6(IP):
            IP = IP.split(':')
            if len(IP) != 8: return False
            for ip in IP:
                if len(ip) > 4 or ip == '': return False
                #if len(ip) == 1 and ip != '0': return False
                for a in ip:
                    if not ('0'<=a<='9' or 'a'<=a<='f' or 'A'<=a<='F'): return False
            return True

        if isIPv4(IP):
            return "IPv4"
        elif isIPv6(IP):
            return "IPv6"
        else:
            return "Neither"


solu = Solution()
print(solu.validIPAddress("1e1.4.5.6"))
print(solu.validIPAddress("192.0.0.1"))
print(solu.validIPAddress("255.178.168.1"))
print(solu.validIPAddress("255.178.168.01"))
print(solu.validIPAddress("255.178.168.1."))
print(solu.validIPAddress("2001:0dbG:85a3:0:0000:8a2e:0370:7334"))
print(solu.validIPAddress("2001:0db8:85a3::0000:8a2e:0370:7334"))
print(solu.validIPAddress("2001:0db8:85a3::0000:8a2e:0370:7334:"))
print(solu.validIPAddress("02001:0db8:85a3:0:0000:8a2e:0370:7334"))
